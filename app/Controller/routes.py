from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app.Model.models import Position
from app.Controller.forms import ResearchPositionForm
from app import db


bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/faculty_index', methods=['GET'])
def faculty_index():
    positions = Position.query.order_by(Position.time_commitment.desc())
    return render_template('f_index.html', title="WSU Research Network",positions=positions.all())

@bp_routes.route('/student_index', methods=['GET'])
def student_index():
    positions = Position.query.order_by(Position.time_commitment.desc())
    return render_template('s_index.html', title = "WSU Research Network",positions=positions.all())

@bp_routes.route('/newPost', methods=['GET', 'POST'])
def postReasearch():
    postform = ResearchPositionForm()
    if postform.validate_on_submit():
        newPost = Position(title=postform.research_title.data, desc=postform.desc.data, start_date=postform.start_date.data,
        end_date=postform.end_date.data, time_commitment=postform.time_commitment.data, research_field=postform.research_field.data, 
        applicant_qualification=postform.applicant_qualification.data)
        
        db.session.add(newPost)
        db.session.commit()
        flash("Your research position:  " + newPost.title + " is created! ")
    return render_template('newPost.html', form = postform)
