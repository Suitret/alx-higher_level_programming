#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments.

// Check if the API URL was provided as an argument.
if (!apiUrl) {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Initialize an object to store the count of completed tasks for each user.
const completedTasksByUser = {};

// Make a GET request to the specified API URL.
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    // Loop through the todos and count completed tasks by user.
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    // Print the completed tasks by user.
    console.log(completedTasksByUser);
  } else {
    console.error('HTTP request failed. Status code:', response.statusCode);
  }
});
