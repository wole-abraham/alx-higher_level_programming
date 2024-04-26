#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let times = 0;

  for (const items of list) {
    if (items === searchElement) {
      times += 1;
    }
  }
  return times;
};
