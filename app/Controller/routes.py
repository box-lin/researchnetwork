from operator import pos
from collections import defaultdict
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app.Model.models import Position,User, Apply
from app.Controller.forms import FacultyEditProfileForm, ResearchPositionForm, StudentFilterForm, StudentEditProfileForm, FacultyFilterForm
from flask_login import current_user, login_required
from app import db
from Constant import researchtopics


bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


#--------------------------------- Helper Method -----------------------------------------#

'''
@param <student user> <all positions from db>
@return <ordered list of position from high matched research areas to low matched research areas>
'''
def recommandation(student, allpositions):
    # all the position {position:set(topics)} stored in a dictionary.
    postion_topic_pair = defaultdict(set)
    for position in allpositions:
        p_topics = set()
        for topic in position.positiontopics:
            p_topics.add(topic.title)
        postion_topic_pair[position] = p_topics
    
    # student's research topics in a list
    s_topics = list()
    for topic in student.researchtopic:
        s_topics.append(topic.title)
    
    # {position:recomm_level}
    result = {}
    for pos in postion_topic_pair.keys():
        recomm_level = 0
        for s_t in s_topics:
            if s_t in postion_topic_pair[pos]:
                recomm_level += 1
        if recomm_level > 0:
            result[pos] = recomm_level
            
    # rank the positions by recomm level
    if len(result) > 0:
        order_pos_level = sorted(list(result.items()), key = lambda x:x[1], reverse=True)
        order_pos = list(map(lambda x: x[0], order_pos_level))
        return order_pos
    # if no such match found then none post show.
    return []

'''
Filter by corresponding research topics.
'''
def filter_by(sortway, allpositions):
    if sortway == 'Please choose below options:':
        return allpositions
    res = set()  
    for position in allpositions:
        for topic in position.positiontopics:
            if topic.title == sortway: # one position might in multi topic use a set to avoid duplicates
                res.add(position) 
    return list(res)
#====================================================================================#

#------------------------- Faculty Interfaces ---------------------------------------#
'''
Faculty Home Page Route
'''
@bp_routes.route('/faculty_index', methods=['GET','POST'])
@login_required
def faculty_index():
    positions = Position.query.order_by(Position.time_commitment.desc()).all()
    fForm = FacultyFilterForm()
    onlymy = False
    if fForm.validate_on_submit():
        onlymy = fForm.checkbox.data
        sortway = fForm.filter.data
        positions = filter_by(sortway, positions)
    return render_template('f_index.html', title="WSU Research Network",positions=positions, onlymy = onlymy, faculty = current_user, form = fForm)


'''
Faculty's post new position route.
'''
@bp_routes.route('/newPost', methods=['GET', 'POST'])
@login_required
def postReasearch():
    if current_user.is_student():
        return render_template('404error.html', user = current_user)
    postform = ResearchPositionForm()
    if postform.validate_on_submit():
        newPost = Position(title=postform.research_title.data, 
                           desc=postform.desc.data, 
                           start_date=postform.start_date.data,
                           end_date=postform.end_date.data, 
                           time_commitment=postform.time_commitment.data, 
                           applicant_qualification=postform.applicant_qualification.data,
                           user_id=current_user.id)
        for topic in postform.research_field.data:
            newPost.positiontopics.append(topic)
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
Faculty approve student application for interview
'''
@bp_routes.route('/approve/<position_id>/<student_id>', methods=["POST","GET"])
@login_required
def approve(position_id,student_id):
    application = Apply.query.filter_by(positionid=position_id, studentid = student_id).first()
    if application:
        application.status = 2
        db.session.commit()
        flash("Student approved for interview!")
        return redirect(url_for('routes.applicants_list'))
    return redirect(url_for('routes.applicants_list'))
    
'''
Faculty decide to hire student
'''
@bp_routes.route('/hire/<position_id>/<student_id>', methods=["POST","GET"])
@login_required
def hire(position_id, student_id):
    application = Apply.query.filter_by(positionid=position_id, studentid = student_id).first()
    if application:
        application.status = 3
        db.session.commit()
        flash("Student Hire Successfully!")
        return redirect(url_for('routes.applicants_list'))
    return redirect(url_for('routes.applicants_list'))

'''
Faculty decide to reject student
'''
@bp_routes.route('/reject/<position_id>/<student_id>', methods=["POST","GET"])
@login_required
def reject(position_id, student_id):
    application = Apply.query.filter_by(positionid=position_id, studentid = student_id).first()
    if application:
        application.status = 4
        db.session.commit()
        flash("Student Rejected!")
        return redirect(url_for('routes.applicants_list'))
    return redirect(url_for('routes.applicants_list'))

'''
Faculty display profile
'''
@bp_routes.route('/f_profile/', methods = ['GET'])
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

'''
Faculty get student profile
'''
@bp_routes.route('/get_s_profile/<s_id>', methods=['GET'])
@login_required
def get_s_profile(s_id):
    theStudent = User.query.filter_by(id=s_id).first()
    titles = theStudent.firstname + ', ' + theStudent.lastname + " Profile"
    return render_template('s_profile.html', title = titles, student = theStudent)

@bp_routes.route('/get_position_info/<position_id>', methods=['GET'])
@login_required
def get_position_info(position_id):
    thePosition = Position.query.filter_by(id=position_id).first()
    return render_template('position_info.html', position = thePosition)

'''
Faculty modify existing position info
'''
@bp_routes.route('/f_modify_position<position_id>', methods = ['GET','POST'])
@login_required
def f_modify_position(position_id):
    thePosition = Position.query.filter_by(id=position_id).first()
    pform = ResearchPositionForm()
    if request.method == 'POST':
        if pform .validate_on_submit():
            thePosition.title = pform.research_title.data
            thePosition.desc = pform.desc.data
            thePosition.start_date = pform.start_date.data
            thePosition.end_date = pform.end_date.data
            thePosition.time_commitment = pform.time_commitment.data
            thePosition.applicant_qualification = pform.applicant_qualification.data
            for r in thePosition.positiontopics:
                thePosition.positiontopics.remove(r)
            for r in pform.research_field.data:
                thePosition.positiontopics.append(r)
            db.session.add(thePosition)
            db.session.commit()
            flash("Your Position Has Been Updated!")
            return redirect(url_for('routes.faculty_index'))
        pass
    elif request.method == 'GET':
        pform.research_title.data = thePosition.title
        pform.desc.data = thePosition.desc
        pform.start_date.data = thePosition.start_date
        pform.end_date.data = thePosition.end_date
        pform.time_commitment.data = thePosition.time_commitment
        pform.applicant_qualification.data = thePosition.applicant_qualification
        pform.research_field.data = thePosition.positiontopics
    else:
        pass
    return render_template('f_modify_position.html', position = thePosition, form = pform)
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
    onlyapply = False
    if fForm.validate_on_submit():
        onlyapply = fForm.checkbox.data
        sortway = fForm.filter.data
        if sortway == "Recommended Research Opportunities":
            positions = recommandation(current_user, positions)
        else:
            positions = filter_by(sortway, positions)
    return render_template('s_index.html', title = "WSU Research Network", positions=positions, form=fForm, student = current_user, onlyapply = onlyapply)

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
    #TODO: if position is not exist, return error
    return redirect(url_for('routes.student_index'))

@bp_routes.route('/MyProfile/',methods = ['GET'])
@login_required
def My_Profile():
        return render_template('s_profile.html', title = 'My Profile', student = current_user)


'''
Student edit profile
'''
@bp_routes.route('/s_profile_edit', methods = ['GET','POST'])
@login_required
def s_profile_edit():
    eform = StudentEditProfileForm()
    print(current_user)
    if request.method == 'POST':
        #handle the form submission
        if eform.validate_on_submit():
            print(current_user)
            current_user.firstname = eform.firstname.data
            current_user.lastname = eform.lastname.data
            current_user.phone = eform.phone.data
            current_user.wsuid = eform.wsuid.data
            current_user.set_password(eform.password.data)
            current_user.major = eform.major.data
            current_user.GPA = eform.GPA.data
            # current_user.graduationdate = eform.graduation.data
            for i in current_user.elective:
                current_user.elective.remove(i)
            for e in eform.elective.data:
                current_user.elective.append(e)
            for z in current_user.researchtopic:
                current_user.researchtopic.remove(z)
            for r in eform.researchtopic.data:
                current_user.researchtopic.append(r)
            for q in current_user.programming:
                current_user.programming.remove(q)
            for p in eform.programming.data:
                current_user.programming.append(p)
            current_user.research_experience = eform.experience.data
            db.session.add(current_user)
            db.session.commit()
            flash("Your changes have been saved")
            return redirect(url_for('routes.My_Profile'))
        pass
    elif request.method == 'GET':
        eform.firstname.data = current_user.firstname
        eform.lastname.data = current_user.lastname
        eform.phone.data = current_user.phone
        eform.wsuid.data = current_user.wsuid
        eform.major.data = current_user.major
        eform.graduation.data = current_user.graduationdate
        eform.GPA.data = current_user.GPA
        eform.elective.data = current_user.elective
        eform.researchtopic.data = current_user.researchtopic
        eform.programming.data = current_user.programming
        eform.experience.data = current_user.research_experience
    else:
        pass
    return render_template('s_profile_edit.html', title = 'Edit Student Profile', form = eform)

#===============================================================================#