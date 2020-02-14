$(function () {
    $.get("https://fourtonfish.com/hellosalut/?lang=f", function (data) {
        $("div#hello").text(data.hello);
    });
});
