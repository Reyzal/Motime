// All jquery will be runned here
function jquery_run(url) {
    var dateToday = new Date();
    // Creating Datepicker
    $(function () {
        $("#input_datepicker").datepicker({dateFormat: "yy-mm-dd", minDate: dateToday});
    });

    // this will prevent reload on submit
    $('#ot-form').on('submit', function (event) {
        // event.preventDefault();
        create_ot(url);
    });

}


// create ot
function create_ot(url) {
    if ($('#input_ot_type').val() != 'start' && $('#input_hrs').val() != '00') {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: url,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'ot_date': $('#input_datepicker').val(),
                'ot_type': $('#input_ot_type').val(),
                'ot_hrs': $('#input_hrs').val()
            },
            dataType: 'json',
            success: function (data) {
                $('#input_datepicker').val('');
                $('#input_ot_type').val('start');
                $('#input_hrs').val('00');

                // console.log(data.result);
                alert(data.result);
            },
            error: function (data) {
                console.log(data.error);
            }
        });
    } else {
        alert("Please fill up shift type and number of Hrs")
    }
}
