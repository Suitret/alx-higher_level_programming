#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from command line arguments.

// Check if the movie ID was provided as an argument.
if (!movieId) {
  console.error('Usage: node 3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Define the URL for the Star Wars API with the provided movie ID.
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API.
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error('Movie not found. Status code:', response.statusCode);
  }
});
