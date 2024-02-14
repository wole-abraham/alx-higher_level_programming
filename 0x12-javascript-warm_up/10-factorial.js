#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(parseInt(n))) {
    return 1; // Factorial of NaN is 1
  } else if (n <= 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return n * computeFactorial(n - 1); // Recursive case: multiply n by factorial of (n - 1)
  }
}

const input = parseInt(process.argv[2]);
console.log(computeFactorial(input));
