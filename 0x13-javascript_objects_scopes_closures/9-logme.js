#!/usr/bin/node

let count = 0; // Initialize the count outside the function

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
