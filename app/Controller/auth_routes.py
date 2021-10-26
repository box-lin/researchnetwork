from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from wtforms.validators import Email
from config import Config
from app.Controller.auth_forms import LoginForm, FacultyRegistrationForm, StudentRegistrationForm
from app import db
from app.Model.models import User
from flask_login import current_user, login_user, logout_user, login_required


bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

# @bp_auth.route('/register', methods=['GET', 'POST'])
# def register():

'''
Generic Login Route
'''
@bp_auth.route('/', methods = ['GET','POST'])
@bp_auth.route('/login', methods = ['GET','POST'])
def login():
    lform = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('routes.faculty_index')) 
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if user is None or user.get_password(lform.password.data) == False or user.role != lform.role.data:
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember_me.data)
        return redirect(url_for('routes.faculty_index'))
    return render_template('login.html', title = 'Sign In', form=lform)


'''
Logout Route
'''
@bp_auth.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

'''
Faculty Register Route
'''
@bp_auth.route('/faculty_register', methods = ['GET','POST'])
def faculty_register():
    fform = FacultyRegistrationForm()
    if fform.validate_on_submit():
        faculty = User(username=fform.username.data, lastname=fform.lastname.data, firstname=fform.firstname.data, wsuid=fform.wsuid.data,
                       email=fform.email.data, phone=fform.phone.data, role="Faculty")
        faculty.set_password(fform.password.data)
        db.session.add(faculty)
        db.session.commit()
        flash('Congratulations, ' + fform.username.data + ' you have successfully registered!')
        return redirect(url_for('auth.login'))
    return render_template('f_register.html', title = 'Faculty Registration', form = fform)


'''
Student Register Route
'''
@bp_auth.route('/student_register', methods = ['GET','POST'])
def student_register():
    sform = StudentRegistrationForm()
    if sform.validate_on_submit():
        student = User(username=sform.username.data, lastname=sform.lastname.data, firstname=sform.firstname.data, wsuid=sform.wsuid.data,
                       email=sform.email.data, phone=sform.phone.data, major=sform.major.data, GPA=sform.GPA.data, gradulation=sform.gradulation.data,
                       elective=sform.elective.data, researchtopic=sform.researchtopic.data, programming=sform.programming.data, 
                       experience=sform.experience.data, role="Student"
                       )
        student.set_password(sform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, ' + sform.username.data + ' you have successfully registered!')
        return redirect(url_for('auth.login'))
    return render_template('s_register.html', title = 'Student Registration', form = sform)