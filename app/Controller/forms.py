from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import  DataRequired, Email, EqualTo, ValidationError, Length, DataRequired, regexp

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



