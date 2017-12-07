function change_password(url) {
    var csrftoken = getCookie('csrftoken');
    var newPassword = document.getElementById('input_new_pass_confirm').value;


    console.log(newPassword);
    $.ajax({
        url: url,
        type: "POST",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'password': newPassword
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.success);
        },
        error: function (data) {
            console.log(data.error);
        }
    });
}

function checkOldPass(url) {
    var oldPasswordValue = document.getElementById('input_old_pass').value;
    var oldPassword = document.getElementById('oldPassword');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";

    $.ajax({
        url: url,
        type: "GET",
        data: {
            'password': oldPasswordValue
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_correct) {
                oldPassword.style.backgroundColor = goodColor;
                message.style.color = goodColor;
                message.innerHTML = "Passwords Match!"
            }
        },
        error: function (data) {
            console.log(data.error);
        }
    });
}

// check if new pass and confirm pass are the same
function checkPass() {
    var pass1 = document.getElementById('input_new_pass');
    var pass2 = document.getElementById('input_new_pass_confirm');

    var message = document.getElementById('confirmMessage3');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";

    if (pass1.value == pass2.value) {
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match!"
    } else {
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
}

// check new password quality
function check_password_quality() {
    var newPassword = document.getElementById('input_new_pass').value;
    var input_new_pass = document.getElementById('input_new_pass');

    var message = document.getElementById('confirmMessage2');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";

    var hasNumbers = /\d/;

    // check if password has numbers
    if (hasNumbers.test(newPassword)) {
        input_new_pass.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = ""
    } else {
        input_new_pass.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords must contain numbers"
    }

    // check if password is 8 characters long
    if (newPassword.length < 8) {
        input_new_pass.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Must be 8 characters long"
    } else {
        input_new_pass.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = ""
    }
}

