from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app.Model.models import Position,User,Apply
from app.Controller.forms import FacultyEditProfileForm, ResearchPositionForm, StudentFilterForm
from flask_login import current_user, login_required
from app import db


bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


#------------------------- Faculty Interfaces ---------------------------------------#
'''
Faculty Home Page Route
'''
@bp_routes.route('/faculty_index', methods=['GET'])
@login_required
def faculty_index():
    positions = Position.query.order_by(Position.time_commitment.desc())
    return render_template('f_index.html', title="WSU Research Network",positions=positions.all())


'''
Faculty's post new position route.
'''
@bp_routes.route('/newPost', methods=['GET', 'POST'])
@login_required
def postReasearch():
    postform = ResearchPositionForm()
    if postform.validate_on_submit():
        newPost = Position(title=postform.research_title.data, 
                           desc=postform.desc.data, 
                           start_date=postform.start_date.data,
                           end_date=postform.end_date.data, 
                           time_commitment=postform.time_commitment.data, 
                           research_field=postform.research_field.data, 
                           applicant_qualification=postform.applicant_qualification.data,
                           user_id=current_user.id)
        
        db.session.add(newPost)
        db.session.commit()
        flash("Your research position:  " + newPost.title + " is created! ")
        return redirect(url_for('routes.faculty_index'))
    return render_template('newPost.html', form = postform)



'''
Faculty's delete position route.
'''
@bp_routes.route('/delete/<position_id>', methods=['POST','DELETE'])
@login_required
def delete(position_id):
    thePost = Position.query.filter_by(id=position_id).first()
    if thePost:
        db.session.delete(thePost)
        db.session.commit()
        flash("Your Research Position:  " + thePost.title + " has been deleted! ")
        return redirect(url_for('routes.faculty_index'))


'''
Faculty see all applicants for a paticular position
'''
@bp_routes.route('/applicants/<position_id>', methods = ['GET'])
@login_required
def applicants(position_id):
    thePost = Position.query.filter_by(id=position_id).first()
    title_str = "Applicants for " + thePost.title
    return render_template('applicants.html', title = title_str , current_position = thePost)


'''
Faculty review applicant list for all position posted
'''
@bp_routes.route('/applicants_list', methods = ['GET'])
@login_required
def applicants_list():
    position = current_user.get_faculty_posts()
    return render_template('f_applicant_list.html', title = 'Applicant List', pform = position)


'''
Faculty display profile
'''
@bp_routes.route('/f_profile', methods = ['GET'])
@login_required
def f_profile():
    return render_template('f_profile.html', title='Faculty Profile', faculty = current_user)

'''
Faculty edit profile
'''
@bp_routes.route('/f_profile_edit', methods = ['GET','POST'])
@login_required
def f_profile_edit():
    eform = FacultyEditProfileForm()
    if request.method == 'POST':
        #handle the form submission
        if eform.validate_on_submit():
            current_user.firstname = eform.firstname.data
            current_user.lastname = eform.lastname.data
            current_user.wsuid = eform.wsuid.data
            current_user.phone = eform.phone.data
            current_user.email = eform.email.data
            current_user.set_password(eform.password.data)
            db.session.add(current_user)
            db.session.commit()
            flash("Your changes have been saved")
            return redirect(url_for('routes.f_profile'))
        pass
    elif request.method == 'GET':
        eform.firstname.data = current_user.firstname
        eform.lastname.data = current_user.lastname
        eform.wsuid.data = current_user.wsuid
        eform.phone.data = current_user.phone
        eform.email.data = current_user.email
    else:
        pass
    return render_template('f_profile_edit.html', title = 'Edit Faculty Profile', form = eform)

@bp_routes.route('/get_s_profile/<s_id>', methods=['GET'])
@login_required
def get_s_profile(s_id):
    theStudent = User.query.filter_by(id=s_id).first()
    titles = theStudent.firstname + ', ' + theStudent.lastname + " Profile"
    return render_template('s_profile.html', title = titles, student = theStudent)
# ==================================================================================#


# ----------------------------------- Student Interface ----------------------------#
'''
Student Home Page Route
'''
@bp_routes.route('/student_index', methods=['GET','POST'])
@login_required
def student_index():
    fForm = StudentFilterForm()
    positions = Position.query.order_by(Position.time_commitment.desc()).all()
    if fForm.validate_on_submit():
        flash("filter need to implement")
    return render_template('s_index.html', title = "WSU Research Network", positions=positions, form=fForm)

'''
Student Apply Position route.
'''
@bp_routes.route('/apply/<position_id>', methods=['POST'])
@login_required
def apply(position_id):
    thePost = Position.query.filter_by(id=position_id).first()
    if thePost:
        current_user.apply(thePost)
        db.session.commit()
        flash('You have applied ' + thePost.title +' !')
        return redirect(url_for('routes.student_index'))

'''
Student withdraw application route.
'''
@bp_routes.route('/withdraw/<position_id>', methods=['POST'])
@login_required
def withdraw(position_id):
    thePost = Position.query.filter_by(id=position_id).first()
    if thePost:
        current_user.withdraw(thePost)
        db.session.commit()
        flash('You have withdraw from the ' + thePost.title +' !')
        return redirect(url_for('routes.student_index'))

@bp_routes.route('/MyProfile/',methods = ['GET'])
@login_required
def My_Profile():
        return render_template('s_profile.html', title = 'My Profile', student = current_user)
    
#===============================================================================#