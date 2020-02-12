#!/usr/bin/node
// Movie where character is "wedge Antilles"

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const result = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };
      body = JSON.parse(body);
      for (let i = 0; i < body.length; i++) {
        if (body[i].completed === true) {
          const tmp = result[body[i].userId];
          result[body[i].userId] = tmp + 1;
        }
      }
      console.log(result);
    }
  }
});
