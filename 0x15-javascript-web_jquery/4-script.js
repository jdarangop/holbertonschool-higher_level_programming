function switchColor () {
    if ($("#toggle_header").hasClass("red")) {
        $("#toggle_header").removeClass("red");
        $("#toggle_header").addClass("green");
    } else if ($("#toggle_header").hasClass("green")) {
        $("#toggle_header").removeClass("green");
        $("#toggle_header").addClass("red");
    } else {
        $("#toggle_header").addClass("green");
    }
}
