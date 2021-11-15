from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField,SelectField
from wtforms.fields.core import DateField
from wtforms.validators import  DataRequired, Email, EqualTo, ValidationError, Length, DataRequired, equal_to, regexp
from app.Model.models import User
from wtforms.fields.simple import PasswordField

'''
Flaskform for faculty use - Research position post
'''
class ResearchPositionForm(FlaskForm):
    research_title = StringField('Research Project Title', validators=[DataRequired(),Length(min=0, max=2048)])
    desc = TextAreaField('Project Brif Description', validators=[DataRequired(),Length(min=0, max=2048)])
    start_date = StringField('Start date ', validators=[DataRequired(), Length(min=0, max=128)])
    end_date = StringField('End date ', validators=[DataRequired(), Length(min=0, max=128)])
    time_commitment = StringField('Required Time Commitment',validators=[DataRequired(),Length(min=0, max=128)] )
    research_field = StringField('Research Field', validators=[DataRequired(), Length(min=0, max=128)])
    applicant_qualification = TextAreaField('Applicant Qualification', validators=[DataRequired(),Length(min=0, max=128)])
    submit = SubmitField('Post')

'''
Stutdent Filter Postition form
'''
class StudentFilterForm(FlaskForm):
    filter = SelectField('Filter By', choices = ['Research areas']) 
    checkbox = BooleanField('Display my applied position only')
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
    submit = SubmitField('Register As Faculty')

    # Check for the uniqueness for email
    def validate_email(self, email):
        faculty = User.query.filter_by(email = email.data).first()
        if faculty is not None:
            if faculty.email != email.data:
                raise ValidationError('The email already existed! Please use a different email address.')

    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            if user.wsuid != wsuid.data:
                raise ValidationError('The WSUID already existed! Please use a differen WSUID!')