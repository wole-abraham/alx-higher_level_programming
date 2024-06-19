#!/usr/bin/node

if (process.argv.length - 2 === 0) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
