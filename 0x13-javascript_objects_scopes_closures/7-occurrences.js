#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter variable to count occurrences
  let count = 0;

  // Iterate through the list and count occurrences of the search element
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
