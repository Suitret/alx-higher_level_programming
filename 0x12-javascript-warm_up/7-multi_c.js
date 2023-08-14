#!/usr/bin/node

const inputValue = process.argv[2];
const intValue = parseInt(inputValue);

if (isNaN(intValue)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < intValue) {
    console.log('C is fun');
    i++;
  }
}
