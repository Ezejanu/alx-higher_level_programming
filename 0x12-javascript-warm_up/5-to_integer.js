#!/usr/bin/node

const argv = process.argv;
let intValue;

if (argv[2] !== undefined) {
  intValue = parseInt(argv[2]);
}
if (!isNaN(intValue)) {
  console.log('My number:', intValue);
} else {
  console.log('Not a number');
}
