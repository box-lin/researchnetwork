from flask import Blueprint
from flask import render_template
from config import Config
from app.Controller.auth_forms import LoginForm
from app import db


bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

# @bp_auth.route('/register', methods=['GET', 'POST'])
# def register():

@bp_auth.route('/login', methods = ['GET'])
def login():
    lform = LoginForm()
    return render_template('login.html', title = 'Sign In', form=lform)
