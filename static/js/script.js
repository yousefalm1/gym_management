function confirmJoin() {
    return confirm("Are you sure you want to join this class?");
}


function confirmCancel() {
    return confirm("Are you sure you want to cancel this class?");
}

// Staff area

document.getElementById('showUsersBtn').addEventListener('click', function () {
    document.getElementById('userList').style.display = (userList.style.display === 'none') ? 'block' : 'none';
});

document.getElementById('showClassesBtn').addEventListener('click', function () {
    var classList = document.getElementById('classList');
    classList.style.display = (classList.style.display === 'none' ) ? 'block' : 'none';
});

document.getElementById('showInstructorBtn').addEventListener('click', function (){
    var instructorList = document.getElementById('instructorList');
    instructorList.style.display = (instructorList.style.display === 'none') ? 'block' :'none';
    
})

var classButtons = document.querySelectorAll('.showUsersBtn');
classButtons.forEach(function (button) {
    button.addEventListener('click', function () {

        var classUserList = button.nextElementSibling;

        classUserList.style.display = (classUserList.style.display === 'none') ? 'block' : 'none';
    });
});

