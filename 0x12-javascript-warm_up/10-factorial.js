#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1 || n === 0 || !n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(arg));
