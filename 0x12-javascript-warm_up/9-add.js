#!/usr/bin/node

function add (a, b) {
  const f = parseInt(b);
  const g = parseInt(a);
  console.log(f + g);
}

const num = process.argv;
add(num[2], num[3]);
