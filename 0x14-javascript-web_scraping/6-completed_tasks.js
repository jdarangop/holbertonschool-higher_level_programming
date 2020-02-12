#!/usr/bin/node
// Movie where character is "wedge Antilles"

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const result = {};
      body = JSON.parse(body);
      for (let i = 0; i < body.length; i++) {
        if (result[body[i].userId] === undefined) {
          result[body[i].userId] = 0;
        }
        if (body[i].completed === true) {
          const tmp = result[body[i].userId];
          result[body[i].userId] = tmp + 1;
        }
      }
      console.log(result);
    }
  }
});
