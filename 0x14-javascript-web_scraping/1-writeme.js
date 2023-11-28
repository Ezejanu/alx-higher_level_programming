#!/usr/bin/node
// A script that writes a string to a file

// Import FileSystem
const fs = require('fs');

// Get the file path from the command line argument
const filepath = process.argv[2];
const filecontent = process.argv[3];

// Write the file in utf-8
fs.writeFile(filepath, filecontent, 'utf-8', (err) => {
  // Handle errors, if any
  if (err) {
    console.error(err);
  }
}
);
