from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.fields.core import  RadioField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import TextAreaField 
from wtforms.validators import DataRequired, Email, Length, ValidationError, equal_to
from app.Model.models import ProgrammingLanguages, ResearchTopics, User, TechnicalElectives
from wtforms.ext.sqlalchemy.fields import QuerySelectField

'''
User login form component
'''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = RadioField('Role: ', choices=['Student','Faculty'], validators=[DataRequired()], default='Student')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
Faculty registration form component
'''
class FacultyRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    submit = SubmitField('Register As Faculty')

    def validate_username(self, username):
        faculty = User.query.filter_by(username = username.data).first()
        if faculty is not None:
            raise ValidationError('The username already existed! Please use a different username.')

    # Check for the uniqueness for email
    def validate_email(self, email):
        faculty = User.query.filter_by(email = email.data).first()
        if faculty is not None:
            raise ValidationError('The email already existed! Please use a different email address.')

    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            raise ValidationError('The WSUID already existed! Please use a differen WSUID!')


def get_programming():
    return ProgrammingLanguages.query.all()

def get_researchtopic():
    return ResearchTopics.query.all()

def get_TechnicalElectives():
    return TechnicalElectives.query.all()

def get_programmingLable(theProgramming):
    return theProgramming.name

def get_researchtopicLabel(research):
    return research.title

def get_TechnicalElectivesLabel(theElectives):
    return theElectives.title

'''
Student registration form component
'''
class StudentRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    major = StringField('Major', validators=[DataRequired()])
    GPA = StringField('GPA', validators=[DataRequired()])
    gradulation = DateField('Gradulation Date', format='%Y-%m-%d')
    elective = QuerySelectField('Research Topics', query_factory = get_TechnicalElectives, get_label = get_TechnicalElectivesLabel, allow_blank=False)
    researchtopic = QuerySelectField('Research Topics', query_factory = get_researchtopic, get_label = get_researchtopicLabel, allow_blank=False)
    programming = QuerySelectField('Programming Languages', query_factory = get_programming, get_label = get_programmingLable, allow_blank=False)
    experience = TextAreaField('Experience: ',validators=[DataRequired()])
    submit = SubmitField('Register As Student')

    def validate_username(self, username):
        student = User.query.filter_by(username = username.data).first()
        if student is not None:
            raise ValidationError('The username already existed! Please use a different username.')

    # Check for the uniqueness for email
    def validate_email(self, email):
        student = User.query.filter_by(email = email.data).first()
        if student is not None:
            raise ValidationError('The email already existed! Please use a different email address.')

    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            raise ValidationError('The WSUID already existed! Please use a differen WSUID!')

    def validate_gradulation(self, gradulationdate):
        if gradulationdate.data < date.today():
            raise ValidationError("Graduation date must later than today!")


'''
Registration form component
'''
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     lastname = StringField('Last Name', validators=[DataRequired()])
#     firstname = StringField('First Name', validators=[DataRequired()])
#     wsuid = StringField('WSU ID', validators=[DataRequired()])
#     phone = StringField('Phone Number', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
#     major = StringField('Major', validators=[DataRequired()])
#     GPA = StringField('GPA', validators=[DataRequired()])
#     gradulation = StringField('Gradulation Date', validators=[DataRequired()])
#     elective = TextAreaField('Eletive Courses: ',validators=[DataRequired()])
#     researchtopic = StringField('Research Topics', validators=[DataRequired()])
#     programming = StringField('Programming Languages', validators=[DataRequired()])
#     experience = TextAreaField('Eletive Courses: ',validators=[DataRequired()])
#     submit = SubmitField('Register As Student')

#     def validate_username(self, username):
#         user = User.query.filter_by(username = username.data).first()
#         if user is not None:
#             raise ValidationError('The username already existed! Please use a different username.')

#     # Check for the uniqueness for email
#     def validate_email(self, email):
#         user = User.query.filter_by(email = email.data).first()
#         if user is not None:
#             raise ValidationError('The email already existed! Please use a different email address.')

#     def validate_WSUID(self, wsuid):
#         user = User.query.filter_by(wsuid = wsuid.data).first()
#         if user is not None:
#             raise ValidationError('The WSUID already existed! Please use a differen WSUID!')

