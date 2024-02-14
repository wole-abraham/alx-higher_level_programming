#!/usr/bin/node

const argv = process.argv.length - 2;

if (argv === 0) {
  console.log('undefined is undefined');
} else if (argv === 1) {
  const string = process.argv[2] + ' is undefined';

  console.log(string);
} else if (argv === 2) {
  const string = process.argv[2] + ' is ' + process.argv[3];
  console.log(string);
}
