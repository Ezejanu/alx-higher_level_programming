#!/usr/bin/node

let format = " is ";
const argv = process.argv;

if (argv[2] === undefined) {
  console.log("undefined" + format + "undefined");
} else if (argv.length === 3) {
  console.log(argv[2] + format + "undefined");
} else {
  console.log(argv[2] + format + argv[3]);
}
