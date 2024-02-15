#!/usr/bin/node
// 9-logme.js

// Initialize a counter variable to keep track of the number of arguments printed
let count = 0;

// Function to print the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  // Print the count and the current argument value
  console.log(`${count}: ${item}`);

  // Increment the counter for the next argument
  count++;
};
