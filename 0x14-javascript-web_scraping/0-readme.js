#!/usr/bin/node
// A script that reads and prints the content of a file

// Import FileSystem
const fs = require('fs');

// Get the file path from the command line argument
const filepath = process.argv[2];

// Read the file in utf-8
fs.readFile(filepath, 'utf-8', (err, data) => {
  // Handle errors, if any
  if (err) {
    console.error(err);
    return;
  }

  // Print the content of the file
  console.log(data);
}
);
