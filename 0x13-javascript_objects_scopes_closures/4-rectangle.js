#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w = this.width, h = this.height) {
    for (let i = 0; i < h; i++) {
      let x = '';

      for (let j = 0; j < w; j++) {
        x += 'X';
      }

      console.log(x);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
