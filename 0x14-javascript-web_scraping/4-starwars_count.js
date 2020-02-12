#!/usr/bin/node
// Movie where character is "wedge Antilles"

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      let counter = 0;
      const results = JSON.parse(body).results;
      for (let i = 0; i < results.length; i++) {
        const characters = results[i].characters;
        for (let j = 0; j < characters.length; j++) {
          if (characters[j] === 'https://swapi.co/api/people/18/') {
            counter++;
          }
        }
      }
      console.log(counter);
    }
  }
});
