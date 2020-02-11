#!/usr/bin/node
// Calulate a new array

const list = require('./100-data').list;

console.log(list);
console.log(list.map((element, index) => element * index));
