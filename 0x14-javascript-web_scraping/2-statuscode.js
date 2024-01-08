#!/usr/bin/node
const request = require('request');

const url = process.argv[2]; // Get the URL from command line arguments.

// Check if the URL was provided as an argument.
if (!url) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the specified URL.
request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
