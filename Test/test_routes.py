from datetime import datetime
import os
import pytest
from sqlalchemy.orm import query
from app import create_app, db
from app.Model.models import User,Apply,Position,ProgrammingLanguages,ResearchTopics,TechnicalElectives
from config import Config

class TestConfig(Config):
    SQLAlCHEMY_DATABASE_URL = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=TestConfig)
    db.init_app(flask_app)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

def new_students_user(uname,uemail,utype,uphone,ufirstname,ulastname,uwsuid,umajor,uGPA,ugraduationdate,uResearchEx,uElective,uResearchTopic,uProgramm,paword):
    suser = User(username=uname,email=uemail,usertype=utype,phone=uphone,firstname=ufirstname,lastname=ulastname,wsuid=uwsuid,major=umajor,GPA=uGPA,graduationdate=ugraduationdate,research_experience=uResearchEx,elective=uElective,researchtopic=uResearchTopic,programming=uProgramm)
    suser.set_password(paword)
    return suser

def new_faculty_user(uname,uemail,utype,ufirstname,ulastname,uwsuid,uphone,paword):
    fuser = User(username=uname,email=uemail,usertype=utype,firstname=ufirstname,lastname=ulastname,wsuid=uwsuid,phone=uphone)
    fuser.set_password(paword)
    return fuser

def init_elective():
    if TechnicalElectives.query.count() == 0:
        elective = ['Test1','Test2','Test3']
        for e in elective:
            db.session.add(TechnicalElectives(title=e))
        db.session.commit()
    return None

def init_programming():
    if ProgrammingLanguages.query.count() == 0:
        pragromming = ['Java','C++','C#','Haskell','R','Python','C','Golang','Swift','Javascript','MATLAB','PHP','Ruby','Delphi','SQL']
        for p in pragromming:
            db.session.add(ProgrammingLanguages(name=p))
        db.session.commit()
    return None

def init_researchtopic():
    if ResearchTopics.query.count() == 0:
        topic = ['Electronic Design Automation','High Performance Computing (HPC) and Scalable Data Science','Artificial Intelligence and Machine Learning','Bioinformatics','Distributed and Networked Systems','Power Engineering','Systems Engineering','Software Engineering']
        for t in topic:
            db.session.add(ResearchTopics(title=t))
        db.session.commit()
    return None

@pytest.fixture
def init_database():
    db.create_all()
    init_elective()
    init_programming()
    init_researchtopic()
    
    elective = db.session.query(TechnicalElectives).filter_by(title="Test1")
    researchtopic = db.session.query(ResearchTopics).filter_by(title="Bioinformatics")
    programming = db.session.query(ProgrammingLanguages).filter_by(name="C++")
    user1 = new_students_user(uname='luuis',uemail='luuis1234567@163.com',utype=0,uphone='4253260389',ufirstname='Yi',
                              ulastname='Chou',uwsuid='011744816',umajor='CS',uGPA='3.0',ugraduationdate=datetime(2021,12,22),
                              uResearchEx='test',uElective=elective,uResearchTopic=researchtopic,uProgramm=programming,paword='123')
    user2 = new_faculty_user(uname='louis',uemail='gan80middle@163.com',utype=1,ufirstname='Yi',ulastname='Chou',uwsuid='123456789',
                             uphone='4253260387',paword='123')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    yield
    db.drop_all()

def test_register_page(test_client, init_database):
    response=test_client.get('/register')
    assert True

def test_student_register(test_client,init_database):
    elective1 = list( 
                     map (
                         lambda x: x.title , filter(lambda x: x.title == "Test1", TechnicalElectives.query.all())
                         )
                    )
    researchtopic1 = list( 
                        map (
                            lambda x: x.title , filter(lambda x: x.title == 'Bioinformatics', TechnicalElectives.query.all())
                            )
                         )
    
    programming1 = list( 
                        map (
                            lambda x: x.title , filter(lambda x: x.title == 'C++', TechnicalElectives.query.all())
                            )
                        )

    response = test_client.post('/register',
                            data = dict(username='test1',email='test1@gmail.com',phone='1234567890',firstname='Yi',lastname='Chou',
                                        wsuid='1234567890',major='CS',GPA='3.0',gradulation=datetime(2021,12,22).strftime('%Y-%m-%d'),experience='test',
                                        elective=elective1,researchtopic=researchtopic1,programming=programming1,password="goodgood",password2="goodgood"),
                            follow_redirects=True)
    
    assert response.status_code == 200
    s = db.session.query(User).filter(User.username=='test1')
    assert s.first().email == 'test1@gmail.com'
    assert s.first().usertype == 0
    assert s.first().phone == '1234567890'
    assert s.first().firstname == 'Yi'
    assert s.first().lastname == 'Chou'
    assert s.first().wsuid == 1234567890
    assert s.first().major == 'CS'
    assert s.first().GPA == 3.0
    assert s.first().graduationdate == datetime(2021,12,22)
    assert s.first().research_experience == 'test'
    
    for i, e in enumerate(s.first().elective):
        assert e == elective1[i]
        
    for i, r in enumerate(s.first().researchtopic):
        assert r == researchtopic1[i]
        
    for i, p in enumerate(s.first().programming):
        assert p == researchtopic1[i]
    assert s.count() == 1
    # assert b"Sign In" in response.data

def test_faculty_register(test_client,init_database):
    response = test_client.post('/register',
                        data=dict(username='test2',email='test2@gmail.com',usertype=1,firstname='Yi',lastname='Chou',wsuid='2345678901',phone='4253260387',password='123',password2='123'),
                        follow_redirects=True)
    assert response.status_code == 200
    f = db.session.query(User).filter(User.username=='test2')
    assert f.first().email == 'test2@gmail.com'
    assert f.first().usertype == 1
    assert f.first().phone == '4253260387'
    assert f.first().firstname == 'Yi'
    assert f.first().lastname == 'Chou'
    assert f.first().wsuid == 2345678901
    assert f.count() == 1
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data

def test_invalidlogin(test_client,init_database):
    response = test_client.post('/login',
                                data=dict(username='jack',password='1234567',remember_me=False),
                                follow_redirects=True)
    assert response.status_code == 200
    # assert b"Invalid username or password" in response.data

def test_login_logout(request,test_client,init_database):
    response = test_client.post('/login',
                                data=dict(username='luuis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Welcome to Research Position" in response.data

    response = test_client.get('/logout',follow_redirects=True)
    assert response.status_code == 200
    # assert b"Sigh in" in response.data
    # assert b"Please log in to access this page." in response.data

def test_new_position_post(test_client,init_database):
    response = test_client.post('/login',
                                data=dict(username='louis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Welcome to Research topic" in response.data

    response = test_client.get('/newPost')
    assert response.status_code == 200
    # assert b"Post New Research position" in response.data

    faculty = db.session.query(User).filter(User.username=='louis').first()

    research_field1 = db.session.query(ResearchTopics).filter_by(title='Bioinformatics')
    
    # response = test_client.post('/newPost',
    #                             data=dict(title='title',desc='decription',start_date=datetime(2021, 12, 22),end_date=datetime(2021, 12, 31),time_commitment='12days',research_field=research_field1, applicant_qualification='test', user_id = faculty.id),
    #                             follow_redirects=True)
    response = test_client.post('/newPost',
                                data=dict(research_title='title',desc='decription',start_date='2021-12-21',end_date='2021-12-31',time_commitment='12days',research_field=research_field1, applicant_qualification='test', user_id = faculty.id),
                                follow_redirects=True)
    assert response.status_code == 200
    # assert b"Welcome to Research Position" in response.data
    # assert b"position post" in response.data
    # assert b"new position post" in response.data
    c = db.session.query(Position).filter(Position.title == 'title')
    assert c.count() >= 1

    response = test_client.get('/logout',follow_redirects=True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data

def test_student_apply_withdraw_position(request,test_client,init_database):
    response = test_client.post('/login',
                                data=dict(username='louis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Hi, Luuis!" in response.data

    faculty = db.session.query(User).filter(User.username=='louis').first()

    research_field1 = db.session.query(ResearchTopics).filter_by(title='Bioinformatics')

    response = test_client.post('/newPost',
                            data=dict(research_title='title',desc='decription',start_date='2021-12-22',end_date='2021-12-31',time_commitment='12days',research_field=research_field1 ,applicant_qualification='test', user_id = faculty.id),
                            follow_redirects=True)
    assert response.status_code == 200
    # assert b"Welcome to Research Position" in response.data
    # assert b"position post" in response.data
    # assert b"new position post" in response.data
    c = db.session.query(Position).filter(Position.title == 'title')
    assert c.count() >= 1

    response = test_client.get('/logout',
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data

    response = test_client.post('/login',
                                data=dict(username='luuis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Hi, Luuis!" in response.data
    

    response = test_client.post('/apply/'+str(c.first().id),
                                data=dict(),follow_redirects=True)
    assert response.status_code == 200
    # assert b"You are apply for a new research position!" in response.data
    c = db.session.query(Position).filter(Position.title == 'title' and Position.research_field == 'test')
    assert c.first().roster[0].studentid == db.session.query(User).filter(User.username=='luuis').first().id

    response = test_client.post('/withdraw/'+str(c.first().id),
                                data=dict(),follow_redirects = True)
    assert response.status_code == 200
    # assert b"You are successfully withdraw a research position!" in response.data
    c = db.session.query(Position).filter(Position.title=='title' and Position.research_field == 'test')
    print(type(c.first().roster))
    assert c.first().roster == []

    response = test_client.get('/logout',
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data

def test_faculty_approve_hire_reject(request,test_client,init_database):
    response = test_client.post('/login',
                                data=dict(username='louis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Hi, Luuis!" in response.data
    
    faculty = db.session.query(User).filter(User.username=='louis').first()

    research_field1 = db.session.query(ResearchTopics).filter_by(title='Bioinformatics')

    response = test_client.post('/newPost',
                            data=dict(research_title='title',desc='decription',start_date='2021-12-22',end_date='2021-12-31',time_commitment='12days',research_field=research_field1,applicant_qualification='test', user_id = faculty.id),
                            follow_redirects=True)
    assert response.status_code == 200
    # assert b"Welcome to Research Position" in response.data
    # assert b"position post" in response.data
    # assert b"new position post" in response.data
    c = db.session.query(Position).filter(Position.title == 'title')
    assert c.count() >= 1

    response = test_client.get('/logout',
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data

    response = test_client.post('/login',
                                data=dict(username='luuis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Hi, Luuis!" in response.data

    response = test_client.post('/apply/'+str(c.first().id),
                                data=dict(),follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/logout',
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data

    response = test_client.post('/login',
                                data=dict(username='louis',password='123',remember_me=False),
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Hi, Luuis!" in response.data
    student = db.session.query(User).filter(User.username=='luuis').first()
    student_id = student.id
    position_id = c.first().id
    print(c.first())
    response = test_client.get('/approve/' + str(position_id) + '/' + str(student_id), data = dict(),follow_redirects = True)
    print('/approve/' + str(position_id) + '/' + str(student_id))
    assert response.status_code == 200
    
    c = db.session.query(Position).filter(Position.id == position_id)
    print(c.first().roster[0].status)
    assert c.first().roster[0].status == 2
    # assert b"You approve this student apply" in response.data

    response = test_client.post('/hire/' + str(position_id) + '/' + str(student_id), data = dict(),follow_redirects = True)
    assert response.status_code == 200
    c = db.session.query(Position).filter(Position.id == position_id)
    assert c.first().roster[0].status == 3
    # assert b"You hire this student" in response.data

    response = test_client.post('/reject/'  + str(position_id) + '/' + str(student_id),data = dict(),follow_redirects = True)
    assert response.status_code == 200
    c = db.session.query(Position).filter(Position.id == position_id)
    assert c.first().roster[0].status == 4
    # assert b"You reject this student" in response.data

    response = test_client.get('/logout',
                                follow_redirects = True)
    assert response.status_code == 200
    # assert b"Sign in" in response.data
    # assert b"Please log in to access this page." in response.data
