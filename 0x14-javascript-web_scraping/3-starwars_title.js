#!/usr/bin/node
// A  script that prints the title of a Star Wars
// movie where the episode number matches a given integer

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error.message);
    return;
  }
  const movieInfo = JSON.parse(body);
  console.log(`${movieInfo.title}`);
}
);
