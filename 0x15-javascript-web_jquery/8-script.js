$(function () {
    $.get("https://swapi.co/api/films/?format=json", function (data) {
        const results = data.results;
        for (let i = 0; i < results.length; i++) {
            $("ul#list_movies").append("<li>" + results[i].title + "</li>");
        }
    })
});
