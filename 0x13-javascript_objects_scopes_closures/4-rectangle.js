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
    rotate () {
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
    }
    double () {
        this.width = this.width * 2;
        this.height = this.height * 2;
    }

}

module.exports = Rectangle;
