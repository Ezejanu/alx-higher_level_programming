#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined || argv.length === 3) {
  console.log('0');
} else {
  const numbers = argv.slice(2).map(Number);
  const descendingOrder = numbers.sort((a, b) => b - a);
  console.log(descendingOrder[1]);
}
