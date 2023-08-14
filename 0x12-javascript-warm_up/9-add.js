#!/usr/bin/node

const inputValue = process.argv[2];
const intValue = parseInt(inputValue);

if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', intValue);
}
