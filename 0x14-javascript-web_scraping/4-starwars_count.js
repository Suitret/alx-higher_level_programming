#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments.

// Check if the API URL was provided as an argument.
if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the specified Star Wars API URL.
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const characterId = 18; // Wedge Antilles' character ID

    // Filter the films where Wedge Antilles (character ID 18) is present.
    const filmsWithWedgeAntilles = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(filmsWithWedgeAntilles.length);
  } else {
    console.error('API request failed. Status code:', response.statusCode);
  }
});
