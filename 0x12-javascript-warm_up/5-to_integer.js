#!/usr/bin/node

const length = process.argv.length - 2;

if (length === 0) {
  console.log('Not a number');
} else {
  const string = parseInt(process.argv[2]);
  if (isNaN(string)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + process.argv[2]);
  }
}
