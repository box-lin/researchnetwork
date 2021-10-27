from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app.Model.models import Position


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