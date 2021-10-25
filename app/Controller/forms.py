from operator import length_hint
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import  DataRequired, Email, EqualTo, ValidationError, Length, DataRequired, regexp

class ResearchPositionForm(FlaskForm):
    research_title = StringField('Research Project Title', [Length(min=0, max=2048)], validators=[DataRequired()])
    desc = StringField('Project Brif Description', [Length(min=0, max=2048)], validators=[DataRequired()])
    start_end_date = StringField('Start date and end date(use / to seprate)', [Length(min=0, max=128)], validators=[DataRequired()])
    time_commitment = StringField('Required Time Commitment',[Length(min=0, max=128)], validators=[DataRequired()] )
    research_field = StringField('Research Field', [Length(min=0, max=128)], validators=[DataRequired()])
    applicant_qualification = StringField('Applicant Qualification', [Length(min=0, max=128)], validators=[DataRequired()])

    def validate_start_end_date(form, start_end_date):
        if start_end_date.find('/'):
            pass
        else:
            raise ValidationError('This field must contain / as a spliter to sperate the start date and end date.')


