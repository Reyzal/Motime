// All jquery will be runned here
function jquery_run(url) {
    var dateToday = new Date();
    // Creating Datepicker
    $(function () {
        $("#input_datepicker").datepicker({dateFormat: "yy-mm-dd", minDate: dateToday});
    });

    // this will prevent reload on submit
    $('#manual-form').on('submit', function (event) {
        // event.preventDefault();
        // create_ot(url);
    });

}