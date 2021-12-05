import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))
import Constant
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import FacultyPositionTopics, Position, ProgrammingLanguages, ResearchTopics, TechnicalElectives, User
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+basedir
    
class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
        
    def test_user_accoun_type(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        self.assertTrue(student.is_student())
    
    def test_user_password_hashing(self):
        faculty = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 1)
        faculty.set_password("123")
        self.assertFalse(faculty.get_password('dsada'))
        self.assertTrue(faculty.get_password('123'))
        
        
    def test_research_topics(self):
        topic = ResearchTopics(title = "new research")
        self.assertEqual(topic.title, "new research")
    
    def test_technical_eletives(self):
        elective = TechnicalElectives(title = "new elective")
        self.assertEqual(elective.title, "new elective")
    
    def test_programming_languages(self):
        pl = ProgrammingLanguages(name = "Java")
        self.assertEqual(pl.name, "Java")
        
    
    def test_researchtopic_in_research_position(self):
        position = Position(title = "reserch1")
        self.assertEqual(position.positiontopics.count(), 0)
        topic1 = ResearchTopics(title = "topicTest1")
        topic2 = ResearchTopics(title = "topicTest2")
        topic3 = ResearchTopics(title = "topicTest3")
        topic4 = ResearchTopics(title = "topicTest4")
        position.positiontopics.append(topic1)
        position.positiontopics.append(topic2)
        position.positiontopics.append(topic3)
        position.positiontopics.append(topic4)
        self.assertEqual(position.positiontopics.count(), 4)
        self.assertEqual(list(map(lambda x: x.title, position.positiontopics.all())), 
                         ['topicTest1', 'topicTest2', 'topicTest3', 'topicTest4'])
 
    
    def test_reseachtopic_in_student(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        self.assertEqual(student.researchtopic.count(), 0)
        topic1 = ResearchTopics(title = "topicTest1")
        topic2 = ResearchTopics(title = "topicTest2")
        topic3 = ResearchTopics(title = "topicTest3")
        topic4 = ResearchTopics(title = "topicTest4")
        student.researchtopic.append(topic1)
        student.researchtopic.append(topic2)
        student.researchtopic.append(topic3)
        student.researchtopic.append(topic4)
        self.assertEqual(student.researchtopic.count(), 4)
        self.assertEqual(list(map(lambda x: x.title, student.researchtopic.all())), 
                    ['topicTest1', 'topicTest2', 'topicTest3', 'topicTest4'])
        
    
    def test_programming_languages_in_student(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        self.assertEqual(student.programming.count(), 0)
        pl1 = ProgrammingLanguages(name="Java")
        pl2 = ProgrammingLanguages(name="Python")
        pl3 = ProgrammingLanguages(name="C")
        pl4 = ProgrammingLanguages(name="C++")
        student.programming.append(pl1)
        student.programming.append(pl2)
        student.programming.append(pl3)
        student.programming.append(pl4)
        self.assertEqual(student.programming.count(), 4)
        self.assertEqual(list(map(lambda x: x.name, student.programming.all())), 
            ['Java', 'Python', 'C', 'C++'])
        

    def test_electives_in_student(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        self.assertEqual(student.elective.count(), 0)
        e1 = TechnicalElectives(title="elective1")
        e2 = TechnicalElectives(title="elective2")
        e3 = TechnicalElectives(title="elective3")
        e4 = TechnicalElectives(title="elective4")
        student.elective.append(e1)
        student.elective.append(e2)
        student.elective.append(e3)
        student.elective.append(e4)
        self.assertEqual(student.elective.count(), 4)
        self.assertEqual(list(map(lambda x: x.title, student.elective.all())), 
            ['elective1', 'elective2', 'elective3', 'elective4'])
        
    def test_student_apply_position(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        self.assertEqual(len(student.application), 0)
        position1 = Position(title = "reserch1")
        position2 = Position(title = "reserch2")
        position3 = Position(title = "reserch3")
        position4 = Position(title = "reserch4")
        student.apply(position1)
        student.apply(position2)
        student.apply(position3)
        student.apply(position4)
        self.assertEqual(len(student.application), 4)
        self.assertEqual(list(map(lambda x: x.applicationapplied.title, student.application)), 
                        ["reserch1", "reserch2", "reserch3", "reserch4"])
        
    
    def test_student_withdraw_position(self):
        student = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 0)
        db.session.add(student)
        db.session.commit()
        
        self.assertEqual(len(student.application), 0)
        
        # add to db, because the way we design to delete track position from db.
        position1 = Position(title = "reserch1")
        db.session.add(position1)
        db.session.commit()
        
        student.apply(position1)
        db.session.commit()
        self.assertEqual(len(student.application), 1)
        
        student.withdraw(position1)
        db.session.commit()
        self.assertEqual(len(student.application), 0)
        
        
    def test_general_student_account(self):
        s_r_topic = ResearchTopics(title = "good topic")
        s_pl = ProgrammingLanguages(name = "Verilog")
        s_elective = TechnicalElectives(title = "Circuit")
        
        student = User(username = "Wanting", lastname = "wu", firstname = "wanting",
                       wsuid = 123, phone = "333333333", GPA = 0.0, major = "CE",
                       email = "wantingw@wsu.edu", usertype = 0)
        
        student.researchtopic.append(s_r_topic)
        student.programming.append(s_pl)
        student.elective.append(s_elective)
        student.set_password("123")
        
        self.assertEqual(student.username, "Wanting")
        self.assertEqual(student.lastname, "wu")
        self.assertEqual(student.firstname, "wanting")
        self.assertEqual(student.phone, "333333333")
        self.assertEqual(student.GPA, 0.0)
        self.assertEqual(student.major, "CE")
        self.assertEqual(student.email, "wantingw@wsu.edu")
        self.assertEqual(student.usertype, 0)
        self.assertEqual(list(map(lambda x: x.title, student.elective.all())), ['Circuit'])
        self.assertEqual(list(map(lambda x: x.name, student.programming.all())), ['Verilog'])
        self.assertEqual(list(map(lambda x: x.title, student.researchtopic.all())), ['good topic'])
        self.assertTrue(student.get_password('123'))
        
    
    def test_general_faculty_account(self):
        faculty = User(username = "Wanting", lastname = "wu", firstname = "wanting",
                       wsuid = 123, phone = "333333333", GPA = 0.0, major = "CE",
                       email = "wantingw@wsu.edu", usertype = 1)
        faculty.set_password("123")
        self.assertEqual(faculty.username, "Wanting")
        self.assertEqual(faculty.lastname, "wu")
        self.assertEqual(faculty.firstname, "wanting")
        self.assertEqual(faculty.phone, "333333333")
        self.assertEqual(faculty.GPA, 0.0)
        self.assertEqual(faculty.major, "CE")
        self.assertEqual(faculty.email, "wantingw@wsu.edu")
        self.assertEqual(faculty.usertype, 1)
        self.assertTrue(faculty.get_password('123'))
    
    def test_general_research_position(self):
        faculty = User(username = "Wanting", email = "wantingw@wsu.edu", usertype = 1)
        db.session.add(faculty)
        db.session.commit()
        self.assertEqual(faculty.get_faculty_posts().all(), [])
        
        topic = ResearchTopics(title = "topicTest")
        position = Position(title = "reserch1", desc = "testing1", start_date = datetime(2022,1,1), 
                            end_date = datetime(2023,1,1), time_commitment = "40hrs/week",
                            applicant_qualification="test qualification", user_id = faculty.id)
        
        position.positiontopics.append(topic)
         
        db.session.add(position)
        db.session.commit()
        self.assertEqual(faculty.get_faculty_posts().count(), 1)
        self.assertEqual(faculty.get_faculty_posts().first().title, "reserch1")
        self.assertEqual(faculty.get_faculty_posts().first().desc, "testing1")
        self.assertEqual(faculty.get_faculty_posts().first().start_date, datetime(2022,1,1))
        self.assertEqual(faculty.get_faculty_posts().first().end_date, datetime(2023,1,1))
        self.assertEqual(faculty.get_faculty_posts().first().time_commitment, "40hrs/week")
        self.assertEqual(faculty.get_faculty_posts().first().applicant_qualification, "test qualification")
        self.assertEqual(faculty.get_faculty_posts().first().positiontopics.count(), 1)
        self.assertEqual(faculty.get_faculty_posts().first().positiontopics.first().title, "topicTest")
         
        
if __name__ == '__main__':
    unittest.main(verbosity=2)