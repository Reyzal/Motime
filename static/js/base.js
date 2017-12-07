// this is for button state
function initialize_btn(action_flag) {
    // flag for button functionality
    switch (action_flag) {
        // did not clock in yet
        case action_flag = 0:
            $('#btn-clockin').show();
            $('#lbl-not-clockin').show();
            $('#div-counter').hide();
            $('#btn-end-lunch').hide();

            $('#btn_clockin').attr('disabled', false);

            $('#btn-clockout').hide();
            $('#btn-lunch').hide();
            $('#btn-lunch-end').hide();

            break;

        // already clock in
        case action_flag = 1:
            $('#btn-clockin').hide();
            $('#lbl-not-clockin').hide();
            $('#btn-lunch-end').hide();
            $('#div-counter').hide();
            $('#btn-end-lunch').hide();

            $('#btn_clockin').attr('disabled', true);

            $('#btn-clockout').show().attr('disabled', true);
            $('#btn-lunch').show();

            break;

        // start break
        case action_flag = 2:
            // $('#LunchModal').modal('show');

            $('#btn-start-lunch').hide();
            $('#btn-cancel-lunch').hide();


            $('#btn-lunch').show();
            $('#div-counter').show();
            $('#btn-end-lunch').show();

            $('#btn_clockin').attr('disabled', true);
            $('#btn-clockout').show().attr('disabled', true);

            break;

        // ended break
        case action_flag = 3:
            $('#btn-clockout').hide();
            $('#btn-lunch').hide();
            $('#btn-lunch-end').hide();
            $('#div-counter').hide();
            $('#btn-end-lunch').hide();

            $('#btn_clockin').attr('disabled', true);

            $('#btn-clockout').show().attr('disabled', false);

            break;

        // clock out
        case action_flag = 4:
            $('#btn-clockout').hide();
            $('#btn-lunch').hide();
            $('#btn-lunch-end').hide();
            $('#btn-clockout').hide();
            $('#div-counter').hide();
            $('#btn-end-lunch').hide();

            $('#btn_clockin').attr('disabled', true);
    }
}


function BtnControl(url, url1, url2) {
    $(document).ready(function () {

        // Clock in dashboard page
        $('#btn-clockin').click(function () {
            $('#btn-clockin').hide();
            $('#lbl-not-clockin').hide();
            $('#btn-lunch').show();
            $('#btn-clockout').show().attr('disabled', true);


            $('#btn_timekeep_in').on('submit', function (event) {
                event.preventDefault();


                // This will get user clock in
                $('#LunchModal').modal('show');

                // clockin(url, $('#btn-clockin').val());
            });
        });
        // End Clock in dashboard page

        // temporary
        $('#btn-question').click(function () {

            $('#btn_timekeep_in').on('submit', function (event) {
                event.preventDefault();

                clockin(url, $('#btn-clockin').val());
            });

        });


        // Lunch dashboard
        $('#btn-lunch').click(function () {
            $('#btn-clockin').hide();
            $('#lbl-not-clockin').hide();

            $('#LunchModal').modal('show');

            $('#btn_clockin').attr("disabled", true);
            $('#btn-clockout').show().attr('disabled', true);

            $('#btn-start-lunch').show();
            $('#btn-cancel-lunch').show();
            $('#btn-lunch').show();

        });
        // End Lunch dashboard

        // Start lunch break
        $('#btn-start-lunch').click(function () {
            $('#btn-start-lunch').hide();
            $('#btn-cancel-lunch').hide();

            // This will start lunch of user
            start_lunch(url2, $('#btn-start-lunch').val());
        });


        // End Lunch dashboard
        $('#btn-lunch-end').click(function () {
            $('#btn-clockin').hide();
            $('#lbl-not-clockin').hide();
            $('#btn-lunch').hide();
            $('#btn-lunch-end').hide();
            $('#btn_clockin').attr("disabled", true);

            $('#btn-clockout').show().attr('disabled', false);

        });
        // End Lunch dashboard

        // Clock out dashboard
        $('#btn-clockout').click(function () {
            $('#btn-clockin').hide();
            $('#lbl-not-clockin').hide();
            $('#btn-lunch').hide();
            $('#btn-clockout').hide();

            // This will get user clock out
            clockout(url1, $('#btn-clockout').val());
        });
        // End Clock out dashboard
    });
}


// Clock in Clock out functions

// -------- Clock in ----------------
function timekeeping_in(url, action) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: url,
        type: "POST",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'action': action
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.result);

        },
        error: function (data) {
            console.log(data.error);
        }
    });
}

function clockin(url, user_action) {
    // this will prevent reload on submit
    $('#btn_timekeep_in').on('submit', function (event) {
        event.preventDefault();
        timekeeping_in(url, user_action);
    });
}

// --------- Clock out ---------------
function timekeeping_out(url, action) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: url,
        type: "POST",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'action': action
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.result);
        },
        error: function (data) {
            console.log(data.error);
        }
    });
}


function clockout(url, action) {
    // this will prevent reload on submit
    $('#btn_timekeep_out').on('submit', function (event) {
        event.preventDefault();
        timekeeping_out(url, action);
    });
}

// End Clock in Clock out functions

function start_break(url, action) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: url,
        type: "POST",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'action': action
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.result);
        },
        error: function (data) {
            console.log(data.error);
        }
    });
}

function start_lunch(url, action) {
    // this will prevent reload on submit
    $('#btn_lunch_in').on('submit', function (event) {
        event.preventDefault();
        start_break(url, action);
    });
}


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
            console.log(c.substring(name.length, c.length));
        }
    }
    return "";
}
