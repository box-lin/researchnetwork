from flask import Blueprint
from config import Config

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route("/")
def hello_world():
    return "<p>Hello, World!</p>"