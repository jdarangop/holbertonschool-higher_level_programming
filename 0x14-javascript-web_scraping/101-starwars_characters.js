#!/usr/bin/node
// Get the status code

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let characters = JSON.parse(body).characters;
    characters = characters.sort(function (a, b) { return parseInt(a.split('/')[5], 10) - parseInt(b.split('/')[5], 10); });
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
