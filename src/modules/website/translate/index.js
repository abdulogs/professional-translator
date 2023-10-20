$(document).on("submit", "#translate", function (e) {
    e.preventDefault();
    const translatetolang = $("#translate-to-lang").val();
    const translatefromlang = $("#translate-from-lang").val();
    const text = $("#translate-to-text").val();

    if (translatetolang == "") {
        return false;
    } else if (translatefromlang == "") {
        return false;
    } else if (text == "" || text == null) {
        msgError("Please enter text to translate...")
        return false;
    } else {
        $.ajax({
            url: BASEURL("api/website/translate/"),
            type: "POST",
            cache: false,
            data: {
                translateto: translatetolang,
                translatefrom: translatefromlang,
                text: text
            },
            headers: {
                'X-CSRFToken': token,
            },
            beforeSend: function () {
                $("#btn-tranlsate").html(`Translating....`);
                $("#btn-tranlsate").prop('disabled', true);
            },
            success: function (data) {
                $("#translate-from-text").val(data.text);
            },
            complete: function () {
                $("#btn-tranlsate").html('Translate');
                $("#btn-tranlsate").prop('disabled', false);
            },
            error: function (response, exception) {
                const data = response.responseJSON
                if (response.status === 0) {
                    msgError('Not connect.\n Verify Network.');
                } else if (response.status == 404) {
                    msgError('Requested page not found. [404]');
                } else if (response.status == 500) {
                    msgError('Internal Server Error [500].');
                } else if (exception === 'parsererror') {
                    msgError('Requested JSON parse failed.');
                } else if (exception === 'timeout') {
                    msgError('Time out error.');
                } else if (exception === 'abort') {
                    msgError('Ajax request aborted.');
                } else if (data["email"]) {
                    msgError(data["email"][0]);
                } else if (data["password"]) {
                    msgError(data["password"][0]);
                } else if (data["non_field_errors"]) {
                    msgError(data["non_field_errors"][0]);
                } else {
                    msgError('Something went wrong!');
                }
            },
        });
    }
});