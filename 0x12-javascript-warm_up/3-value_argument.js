#!/usr/bin/node

const argv = process.argv;
let length = 0;
for (const _ of argv) {
  length = _ - 2;
}
if (length === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
