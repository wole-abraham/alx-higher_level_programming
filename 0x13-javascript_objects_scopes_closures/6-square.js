#!/usr/bin/node

const Squares = require('./5-square.js');

class Square extends Squares {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          x += 'X';
        } else {
          x += 'C';
        }
      }
      console.log(x);
    }
  }
}

module.exports = Square;
