// update profile pic
function update_profile_pic(url) {
    var csrftoken = getCookie('csrftoken');

    // jQuery.noConflict();
    // formdata = new FormData ();
    // jQuery('#inp-file').on("change", function () {
    //     var file = this.file[0];
    //     if(formdata) {
    //         formdata.append("image", file);
    //         jQuery.ajax({
    //             url: url,
    //             type: "POST",
    //             data: formdata,
    //             processData: false,
    //             contentType: false,
    //             success:function () {}
    //         })
    //     }
    // })


    console.log($('#inp-file').value());

    // $.ajax({
    //     url: url,
    //     type: "POST",
    //     data: {
    //         csrfmiddlewaretoken: csrftoken,
    //         'profile_pic': $('#inp-file').val(),
    //     },
    //     dataType: 'json',
    //     success: function (data) {
    //         $('#inp-file').val('');
    //         console.log(data.result);
    //     },
    //     error: function (data) {
    //         console.log(data.error);
    //     }
    // });
}