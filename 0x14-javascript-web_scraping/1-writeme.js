#!/usr/bin/node
// arguments + module fs
const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

// writing to file
fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
