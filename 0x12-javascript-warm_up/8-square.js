#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let i = 0; i < size; i++) {
    let x = '';

    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
