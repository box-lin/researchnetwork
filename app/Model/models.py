from app import db 
from werkzeug.security import generate_password_hash, check_password_hash



'''
User: 
    username, password,

Student:
    contact information (name, last name, WSU ID, email, phone) 
    Enter additional information (major, cumulative GPA, expected graduation date, 
    etc. ) 
    Enter the technical elective courses they completed and the grades they 
    received. 
    Select the research topics they are interested in.  
    Select the programming languages they have experience with.  
    Describe their prior research experience if there is any.  

faculty: 
    Enter contact information (name, last name, WSU ID, email, phone) 
'''

# @login.user_loader
# def load_user(id):
#     role = db.session.get('role')
#     return role_mapping[role].query.get(int(id))


'''
User model consists of <Student> and <Faculty> 
'''
class User(db.Model):

    ## common info ## 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    lastname = db.Column(db.String(20))
    firstname = db.Column(db.String(30))
    wsuid = db.Column(db.Integer, unique = True)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, index=True)

    ## additional student ##
    major = db.Column(db.String(20))
    GPA = db.Column(db.String(5))
    gradulation = db.Column(db.String(10))
    elective = db.Column(db.String(300))
    researchtopic = db.Column(db.String(30))
    programming = db.Column(db.String(30))
    experience = db.Column(db.String(200))

    # role = 1 = student, role = 2 = faculty
    role = db.Column(db.Integer) 
    
    def __repr__(self):
        return '<User {}, {}>'.format(self.id,self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 
    
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_role(self, role):
        return role

class Position(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(2048))
    desc = db.Column(db.String(2048))
    start_date = db.Column(db.String(128))
    end_date = db.Column(db.String(128))
    time_commitment = db.Column(db.String(128))
    research_field = db.Column(db.String(128))
    applicant_qualification = db.Column(db.String(1024))
