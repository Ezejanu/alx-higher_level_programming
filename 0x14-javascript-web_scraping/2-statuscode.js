#!/usr/bin/node
// A script that displays the status code of a GET request.

// Import the request module
const request = require('request');

const URL = process.argv[2];

request.get(URL)
// Attach an event handler to the 'response' event
  .on('response', function (response) {
    // Log the status code to the console
    console.log(`code: ${response.statusCode}`);
  }
  );
