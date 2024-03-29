#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // Get the Movie ID from command line arguments.

// Check if the Movie ID was provided as an argument.
if (!movieId) {
  console.error('Usage: node 100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

// Define the URL for the Star Wars API to retrieve movie details.
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the specified movie URL using the "request" module.
request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    // Fetch the character URLs from the movie data.
    const characterUrls = movieData.characters;

    // Iterate through character URLs and print the character names.
    characterUrls.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
        } else if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error('Movie not found. Status code:', response.statusCode);
  }
});
