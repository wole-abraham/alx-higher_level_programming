#!/usr/bin/node

const list = require('./100-data').list;

const indexList = list.map((x, idx) => x * idx);

console.log(list);
console.log(indexList);
