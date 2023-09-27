#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from command line arguments.
const filePath = process.argv[3]; // Get the file path from command line arguments.

// Check if both URL and file path were provided as arguments.
if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Make a GET request to the specified URL using the "request" module.
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Write the response body to the specified file.
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      }
    });
  } else {
    console.error('HTTP request failed. Status code:', response.statusCode);
  }
});
