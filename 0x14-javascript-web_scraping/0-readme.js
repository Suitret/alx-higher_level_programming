#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line arguments.

// Check if the file path was provided as an argument.
if (!filePath) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

// Read the content of the file in utf-8 encoding.
fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred.
  } else {
    console.log(data); // Print the file content if reading was successful.
  }
});
