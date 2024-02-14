#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv.length - 2 === 0) {
  console.log('Missing size');
} else {
  for (let n = 0; n < size; n++) {
    let x = '';
    for (let i = 0; i < size; i++) {
      x += 'X';
    }
    console.log(x);
  }
}
