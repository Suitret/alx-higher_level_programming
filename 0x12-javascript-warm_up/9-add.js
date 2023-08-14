#!/usr/bin/node

const input1 = process.argv[2];
const int1 = parseInt(input1);
const input2 = process.argv[3];
const int2 = parseInt(input2);

function add (a, b) {
  return (a + b);
}

if (isNaN(int1) || isNaN(int2)) {
  console.log('NaN');
} else {
  console.log(add(int1, int2));
}
