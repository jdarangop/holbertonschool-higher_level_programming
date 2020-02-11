#!/usr/bin/node
// concat two files

const fs = require('fs');

let final = '';

final += fs.readFileSync(process.argv[2]);
final += fs.readFileSync(process.argv[3]);

fs.writeFile(process.argv[4], final, function () {});
