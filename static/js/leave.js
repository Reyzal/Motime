// All jquery will be runned here
function jquery_run(url) {
    var dateToday = new Date();

    // Creating Datepicker
    $(function () {
        $("#input_lv_from").datepicker({dateFormat: "yy-mm-dd"});
        $("#input_lv_to").datepicker({dateFormat: "yy-mm-dd"});
    });

    // this will prevent reload on submit
    $('#lv-form').on('submit', function (event) {
        // event.preventDefault();
        create_lv(url);
    });

}


// create leave
function create_lv(url) {
    if ($('#input_lv_type').val() != 'start' && $('#input_shift').val() != 'start') {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: url,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'lv_date_start': $('#input_lv_from').val(),
                'lv_date_end': $('#input_lv_to').val(),
                'lv_type': $('#input_lv_type').val(),
                'lv_shift': $('#input_shift').val()
            },
            dataType: 'json',
            success: function (data) {
                $('#input_lv_from').val('');
                $('#input_lv_to').val('');
                $('#input_lv_type').val('start');
                $('#input_shift').val('start');

                // console.log(data.result);
                alert(data.result);
            },
            error: function (data) {
                console.log(data.error);
            }
        });
    } else {
        alert("Please fill up leave type and shift")
    }
}