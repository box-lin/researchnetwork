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

function showStudent() {
    clearDisplay();
    document.getElementById("studentForm").style.display = "block";
}

function showFaculty() {
    clearDisplay();
    document.getElementById("facultyForm").style.display = "block";
}

function set_reg_student() {
    jQuery.ajax({
        url: "/set_student",
        method: "POST",
        data: "",
        async: false,
        caches: false,
        success: function(response) {
            // alert("Successfully registered as a student " + response);
        },
        error: function(response) {
            alert("Error: Something went wrong! " + response);
        }
    });
}

function set_reg_faculty() {
    jQuery.ajax({
        url: "/set_faculty",
        method: "POST",
        data: "",
        async: false,
        caches: false,
        success: function(response) {
            // alert("Successfully registered as a faculty " + response);
        },
        error: function(response) {
            alert("Error: Something went wrong! " + response);
        }
    });
}