from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from wtforms.validators import Email
from config import Config
from app.Controller.auth_forms import LoginForm, FacultyRegistrationForm, StudentRegistrationForm
from app import db
from app.Model.models import User


bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

# @bp_auth.route('/register', methods=['GET', 'POST'])
# def register():

'''
Generic Login Route
'''
@bp_auth.route('/', methods = ['GET'])
@bp_auth.route('/login', methods = ['GET'])
def login():
    lform = LoginForm()
    return render_template('login.html', title = 'Sign In', form=lform)

'''
Faculty Register Route
'''
@bp_auth.route('/faculty_register', methods = ['GET','POST'])
def faculty_register():
    fform = FacultyRegistrationForm()
    if fform.validate_on_submit():
        faculty = User(username=fform.username.data, lastname=fform.lastname.data, firstname=fform.firstname.data, wsuid=fform.wsuid.data,
                       email=fform.email.data, role=2)
        faculty.set_password(fform.password.data)
        db.session.add(faculty)
        db.session.commit()
        flash('Congratulations, ' + fform.username.data + ' you have successfully registered!')
        return redirect(url_for('auth_routes.login'))
    return render_template('f_register.html', title = 'Faculty Registration', form = fform)


'''
Student Register Route
'''
@bp_auth.route('/student_register', methods = ['GET','POST'])
def student_register():
    sform = StudentRegistrationForm()
    if sform.validate_on_submit():
        student = User(username=sform.username.data, lastname=sform.lastname.data, firstname=sform.firstname.data, wsuid=sform.wsuid.data,
                       email=sform.email.data, role=1, major=sform.major.data, GPA=sform.GPA.data, gradulation=sform.gradulation.data,
                       elective=sform.elective.data, researchtopic=sform.researchtopic.data, programming=sform.programming.data, 
                       experience=sform.experience.data
                       )
        student.set_password(sform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, ' + sform.username.data + ' you have successfully registered!')
        return redirect(url_for('auth_routes.login'))
    return render_template('s_register.html', title = 'Student Registration', form = sform)