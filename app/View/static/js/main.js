function clearFacultyDisplay() {
    document.getElementById('f_home_page').classList.remove("active");
    document.getElementById('f_post_new_position').classList.remove("active");
    document.getElementById('f_applicant_list').classList.remove("active");
    document.getElementById('f_profile').classList.remove("active")
}

function clearStudentDisplay() {
    document.getElementById('s_home_page').classList.remove("active");
    document.getElementById('s_my_applications').classList.remove("active");
    document.getElementById('s_my_profile').classList.remove("active");
}

function f_home_page_active() {
    document.getElementById('f_home_page').classList.add("active");
}

function f_post_new_position_active() {
    document.getElementById('f_post_new_position').classList.add("active");
}

function f_applicant_list_active() {
    document.getElementById('f_applicant_list').classList.add("active");
}

function f_profile_active() {
    document.getElementById('f_profile').classList.add("active")
}

function s_home_page_active() {
    document.getElementById('s_home_page').classList.add("active")
}