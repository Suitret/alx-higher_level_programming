#!/usr/bin/node

const inputValue = process.argv[2];
const intValue = parseInt(inputValue);

function facto (a) {
  if (a <= 1) { return 1; } else { return a * facto(a - 1); }
}

if (isNaN(intValue) || intValue <= 1) {
  console.log(1);
} else {
  console.log(facto(intValue));
}
