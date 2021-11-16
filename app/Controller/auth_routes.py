from datetime import datetime
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, session
from werkzeug.wrappers import request
from wtforms import validators
from wtforms.validators import Email
from config import Config
from app.Controller.auth_forms import LoginForm, FacultyRegistrationForm, StudentRegistrationForm
from app import db
from app.Model.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask_session import Session


bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

'''
Generic Login Route
'''
@bp_auth.route('/', methods = ['GET','POST'])
@bp_auth.route('/login', methods = ['GET','POST'])
def login():
    lform = LoginForm()
    if current_user.is_authenticated:
        if current_user.usertype == 1: # 1 as faculty
            return redirect(url_for('routes.faculty_index'))
        else:
            return redirect(url_for('routes.student_index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if user is None or user.get_password(lform.password.data) == False:
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember_me.data)
        if user.usertype == 1:
            return redirect(url_for('routes.faculty_index'))
        else:
            return redirect(url_for('routes.student_index'))
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
Register Route
'''
@bp_auth.route('/register', methods = ['GET','POST'])
def register():
    fform = FacultyRegistrationForm()
    sform = StudentRegistrationForm()
    print(fform.data)
    print(sform.data)
    if fform.validate_on_submit() or sform.validate_on_submit():
        if fform.validate_on_submit() and sform.GPA.data == "":
            faculty = User(username=fform.username.data, 
                           lastname=fform.lastname.data, 
                           firstname=fform.firstname.data, 
                           wsuid=fform.wsuid.data,
                           email=fform.email.data, 
                           phone=fform.phone.data, 
                           major="", 
                           GPA=0, 
                           graduationdate=datetime(1971,1,1), 
                           elective="", 
                           researchtopic="", 
                           programming = "", 
                           research_experience="", 
                           usertype=1)
            faculty.set_password(fform.password.data)
            db.session.add(faculty)
            db.session.commit()
            flash('Congratulations, ' + fform.username.data + ' you have successfully registered!')
            return redirect(url_for('auth.login'))
        if sform.validate_on_submit() and sform.GPA.data != "":
            student = User(username=sform.username.data, 
                           lastname=sform.lastname.data, 
                           firstname=sform.firstname.data, 
                           wsuid=sform.wsuid.data,
                           email=sform.email.data, 
                           phone=sform.phone.data, 
                           major=sform.major.data, 
                           GPA=sform.GPA.data, 
                           graduationdate=sform.gradulation.data,
                           research_experience=sform.experience.data, 
                           usertype=0)
            student.set_password(sform.password.data)
            # append programming languages
            for p in sform.programming.data:
                student.programming.append(p)

            # append research topics
            for r in sform.researchtopic.data:
                student.researchtopic.append(r)

            #append elective classes
            for e in sform.elective.data:
                student.elective.append(e)
                
            db.session.add(student)
            db.session.commit()
            flash('Congratulations, ' + sform.username.data + ' you have successfully registered!')
            return redirect(url_for('auth.login'))

    return render_template('register.html', title = 'Registration', fform = fform, sform = sform)