#!/usr/bin/node
// Define the function logMe

exports.converter = function (base) {
  return function (num) {
    return parseInt(num, 10).toString(base);
  };
};
