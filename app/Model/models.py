from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


'''
User model consists of <Student> and <Faculty> 
'''
class User(db.Model, UserMixin):

    ## common info ## 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # usertype =student or faculty
    usertype = db.Column(db.Integer)    #0--student, 1--faculty
    phone = db.Column(db.String(20))
    office = db.Column(db.String(1024))

    # lastname = db.Column(db.String(20))
    # firstname = db.Column(db.String(30))
    # wsuid = db.Column(db.Integer, unique = True)

    ## additional student ##
    major = db.Column(db.String(20))
    GPA = db.Column(db.Float(5))
    gradulationdate = db.Column(db.DateTime)
    research_experience = db.Column(db.String(200))

    elective = db.relationship(
        'TechnicalElectives', secondary = StudentElectives,
        primaryjoin=(StudentElectives.c.user_id == id),lazy='dynamic', overlaps='roster'
    )

    researchtopic = db.relationship(
        'ResearchTopics', secondary = StudentResearchTopics,
        primaryjoin=(StudentResearchTopics.c.user_id == id),lazy='dynamic', overlaps='roster'
    )

    programming = db.relationship(
        'ProgrammingLanguages', secondary = StudentLanguages,
        primaryjoin=(StudentLanguages.c.user_id == id),lazy='dynamic', overlaps='roster'
    )
    

    position = db.relationship('Position', backref='writer', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}, {}>'.format(self.id,self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 
    
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_role(self, role):
        return role

class Applications:
    id = db.Column(db.Integer, primary_key = True)
    position_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.Integer)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(2048))
    desc = db.Column(db.String(2048))
    start_date = db.Column(db.String(128))
    end_date = db.Column(db.String(128))
    time_commitment = db.Column(db.String(128))
    research_field = db.Column(db.String(128))
    applicant_qualification = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    researchtopic = db.relationship(
        'ResearchTopics', secondary = StudentResearchTopics,
        primaryjoin=(StudentResearchTopics.c.user_id == id),lazy='dynamic', overlaps='roster'
    )