#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let a = '';

      for (let j = 0; j < this.width; j++) {
        a += 'X';
      }

      console.log(a);
    }
  }
}

module.exports = Rectangle;
