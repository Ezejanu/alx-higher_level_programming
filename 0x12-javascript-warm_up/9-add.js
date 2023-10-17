#!/usr/bin/node
function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  return result;
}

const argv = process.argv;
console.log(add(argv[2], argv[3]));
