#!/usr/bin/node

const argv = process.argv;
let times;

if (argv[2] !== undefined) {
  times = parseInt(argv[2]);
}
if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= times; i++) {
    let row = '';
    for (let j = 1; j <= times; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
