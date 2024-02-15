#!/usr/bin/node
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  const reversedList = [];

  // Iterate backwards through the original list and push elements into the reversed list
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
