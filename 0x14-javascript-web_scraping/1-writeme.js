#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line arguments.
const contentToWrite = process.argv[3]; // Get the content to write from command line arguments.

// Check if both file path and content to write were provided as arguments.
if (!filePath || !contentToWrite) {
  console.error('Usage: node 1-writeme.js <file-path> "<content-to-write>"');
  process.exit(1);
}

// Write the content to the file in utf-8 encoding.
fs.writeFile(filePath, contentToWrite, 'utf8', (error) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred while writing.
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
