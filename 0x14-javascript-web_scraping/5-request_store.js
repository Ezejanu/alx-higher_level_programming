#!/usr/bin/node
// A script that gets the content of a webpage and stores it in a file

// Import FileSystem and request
const fs = require('fs');
const request = require('request');

// Get the file path from the command line argument
const URL = process.argv[2];
const filepath = process.argv[3];

request(URL)

// Write the response body to the specified file
  .pipe(fs.createWriteStream(filepath));
