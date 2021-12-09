import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import  DataRequired, Email, EqualTo, ValidationError, Length, DataRequired, equal_to, regexp
from app.Model.models import User
from wtforms.widgets import ListWidget, CheckboxInput
from app.Model.models import ProgrammingLanguages, ResearchTopics, User, TechnicalElectives
from wtforms.fields.simple import PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from datetime import date, datetime
from Constant import researchtopics, electives, languages


def get_researchtopic():
    return ResearchTopics.query.all()

def get_researchtopicLabel(research):
    return research.title
'''
Flaskform for faculty use - Research position post

'''
class ResearchPositionForm(FlaskForm):
    research_title = StringField('Research Project Title', validators=[DataRequired(),Length(min=0, max=2048)])
    desc = TextAreaField('Project Brif Description', validators=[DataRequired(),Length(min=0, max=2048)])
    start_date = DateField('Start date ', format='%Y-%m-%d')
    end_date = DateField('End date ', format='%Y-%m-%d')
    time_commitment = StringField('Required Time Commitment',validators=[DataRequired(),Length(min=0, max=128)] )
    research_field = QuerySelectMultipleField('Research Topics', query_factory = get_researchtopic, get_label = get_researchtopicLabel, allow_blank=False)
    applicant_qualification = TextAreaField('Applicant Qualification', validators=[DataRequired(),Length(min=0, max=128)])
    submit = SubmitField('Post')

    def validate_start_date(self, start_date):
        if start_date.data is not None:
            if start_date.data < date.today():
                raise ValidationError("start date must later than today!")

    def validate_end_date(self, end_date):
        if end_date.data is not None:
            if end_date.data < self.start_date.data:
                raise ValidationError("end date must later start date!")



'''
Stutdent Filter Postition form
'''
class StudentFilterForm(FlaskForm):
    filter = SelectField('Filter By', choices= ['Please choose below options:', 'Recommended Research Opportunities'] + researchtopics) 
    checkbox = BooleanField('Display my applied position only')
    refresh = SubmitField('Refresh')

'''
Faculty Filter Position form
'''
class FacultyFilterForm(FlaskForm):
    filter = SelectField('Filter By', choices = ['Please choose below options:'] + researchtopics) 
    checkbox = BooleanField('Display my posted position only')
    refresh = SubmitField('Refresh')

'''
Faculty Edit Profile Form
'''
class FacultyEditProfileForm(FlaskForm):
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    submit = SubmitField('Update Faculty Profile')

    # Check for the uniqueness for email
    def validate_email(self, email):
        faculty = User.query.filter_by(email = email.data).first()
        if faculty is not None:
            if faculty.email != email.data:
                raise ValidationError('The email already existed! Please use a different email address.')

    #Check for the uniqueness for WSUID
    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            if user.wsuid != wsuid.data:
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
Student Edit Profile Form
'''
class StudentEditProfileForm(FlaskForm):
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    major = StringField('Major', validators=[DataRequired()])
    GPA = StringField('GPA', validators=[DataRequired()])
    graduation = DateField('Gradulation Date', format='%Y-%m-%d')
    elective = QuerySelectMultipleField('Technical Electives', query_factory = get_TechnicalElectives, get_label = get_TechnicalElectivesLabel, allow_blank=False, 
                                        widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    researchtopic = QuerySelectMultipleField('Research Topics', query_factory = get_researchtopic, get_label = get_researchtopicLabel, allow_blank=False, 
                                             widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    programming =  QuerySelectMultipleField('Programming Languages', query_factory = get_programming, get_label = get_programmingLable, allow_blank=False, 
                                            widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    experience = TextAreaField('Experience: ',validators=[DataRequired()])
    submit = SubmitField('Update Student Profile')

    # Check for the uniqueness for email
    def validate_email(self, email):
        student = User.query.filter_by(email = email.data).first()
        if student is not None:
            if student.email != email.data:
                raise ValidationError('The email already existed! Please use a different email address.')
    
    # Check the gradulation date must later than today
    def validate_gradulation(self, gradulationdate):
        if gradulationdate.data is not None:
            if gradulationdate.data < date.today():
                raise ValidationError("Graduation date must later than today!")

class ApplicationForm(FlaskForm):
    fullname = StringField('Enter Full Name of the Faculty That Can Provide the Reference for You', validators=[DataRequired()])
    email = StringField('Enter The Email of That Faculty', validators=[DataRequired(),Email()])
    statement = TextAreaField('Brief Statement (describe your interest and what you hope to gain by participating this project)', validators=[DataRequired()])
    submit = SubmitField('Submit Application')