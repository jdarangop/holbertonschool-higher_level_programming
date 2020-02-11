#!/usr/bin/node
// Define the function logMe

let counter = 0;

exports.logMe = function (item) {
  console.log(counter.toString() + ': ' + item);
  counter++;
};
