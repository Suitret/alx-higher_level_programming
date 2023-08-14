#!/usr/bin/node

const inputValue = process.argv[2];
const intValue = parseInt(inputValue);

if (isNaN(intValue)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < intValue) {
    console.log('X'.repeat(intValue));
    i++;
  }
}
