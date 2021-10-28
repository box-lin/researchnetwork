from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.fields.core import RadioField
from wtforms.fields.simple import TextAreaField 
from wtforms.validators import DataRequired, Email, Length, ValidationError, equal_to
from app.Model.models import User

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
    gradulation = StringField('Gradulation Date', validators=[DataRequired()])
    elective = TextAreaField('Eletive Courses: ',validators=[DataRequired()] )
    researchtopic = TextAreaField('Research Topics', validators=[DataRequired()])
    programming = StringField('Programming Languages', validators=[DataRequired()])
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

