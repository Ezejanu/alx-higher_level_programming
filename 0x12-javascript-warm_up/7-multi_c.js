#!/usr/bin/node

const argv = process.argv;
let times;
let i = 1;

if (argv[2] !== undefined) {
  times = parseInt(argv[2]);
}
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  while (i <= times) {
    console.log('C is fun');
    i++;
  }
}
