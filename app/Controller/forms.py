from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField,SelectField
from wtforms.validators import  DataRequired, Email, EqualTo, ValidationError, Length, DataRequired, regexp
from wtforms.fields.html5 import DateField


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

class StudentFilterForm(FlaskForm):
    sortchoice = SelectField('Filter By', choices= [])
    checkbox = BooleanField('Display My Applied Applications')
    refresh = SubmitField('Refresh')

class SrudentProfileForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    GPA = StringField('GPA', validators=[DataRequired()])
    gradulation = DateField('Gradulation Date', format='%Y-%m-%d')
