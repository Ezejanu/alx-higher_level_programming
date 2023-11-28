#!/usr/bin/node
// A script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const APIurl = process.argv[2];
const charID = 18;

request(APIurl, function (error, response, body) {
  if (error) {
    console.error(error.message);
    return;
  }
  const filmInfo = JSON.parse(body);
  const filmsWithWedge = filmInfo.results.filter(film => film.characters.includes(`people/${charID}/`));

  console.log(`${filmsWithWedge.length}`);
});
