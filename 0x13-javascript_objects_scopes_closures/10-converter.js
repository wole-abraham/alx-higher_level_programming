#!/usr/bin/node
// converter.js

// Function to convert a number from base 10 to another base
exports.converter = function (base) {
  // Define a helper function to perform the conversion recursively
  function convertToBase (number) {
    if (number < base) {
      // Base case: if the number is less than the base, return it as a string
      return String(number);
    } else {
      // Recursive case: divide the number by the base and concatenate the remainder
      return convertToBase(Math.floor(number / base)) + String(number % base);
    }
  }

  // Return the helper function to be used externally
  return convertToBase;
};
