#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi.dev/api/films/${process.argv[2]}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movies = JSON.parse(body);
    console.log(`Characters of "${movies.title}":`);

    movies.characters.forEach((characterUrl) => {
      request(characterUrl, function (charError, charResponse, characterBody) {
        if (!charError && charResponse.statusCode === 200) {
          const characters = JSON.parse(characterBody);

          console.log(characters.name);
        } else {
          console.error('Error fetching character data:', charError);
        }
      });
    });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
