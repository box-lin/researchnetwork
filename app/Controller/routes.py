from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/faculty_index', methods=['GET'])
def faculty_index():
    return render_template('f_index.html', title="WSU Research Network")