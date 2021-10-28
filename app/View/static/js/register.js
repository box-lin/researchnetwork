function clearDisplay() {
    document.getElementById("facultyForm").style.display = "none";
    document.getElementById("studentForm").style.display = "none";
    document.getElementById("major").value = "";
    document.getElementById("GPA").value = "";
    document.getElementById("gradulation").value = "";
    document.getElementById("elective").value = "";
    document.getElementById("researchtopic").value = "";
    document.getElementById("programming").value = "";
    document.getElementById("experience").value = "";
}

function showStudent(){
    clearDisplay();
    document.getElementById("studentForm").style.display = "block";
}

function showFaculty(){
    clearDisplay();
    document.getElementById("facultyForm").style.display = "block";
}
