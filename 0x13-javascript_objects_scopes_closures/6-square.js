#!/usr/bin/node

const Squares = require('./5-square');

class Square extends Squares {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let x = '';

        for (let j = 0; j < this.width; j++) {
          x += 'C';
        }
        console.log(x);
      }
    }
  }
}

module.exports = Square;
