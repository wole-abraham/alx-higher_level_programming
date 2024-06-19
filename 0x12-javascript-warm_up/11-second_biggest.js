#!/usr/bin/node

/*
 * sorting a list and slecting the seconfb biggest
 */

const arr = process.argv.slice(2);

function sort (arr) {
  let biggest = 0;
  let secBig = 0;

  if (process.argv.length - 2 === 0 || process.argv.length - 2 === 1) {
    return 0;
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > biggest) {
      biggest = arr[i];
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > secBig && arr[i] !== biggest) {
      secBig = arr[i];
    }
  }

  return secBig;
}
console.log(sort(arr));
