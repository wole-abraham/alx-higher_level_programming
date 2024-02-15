#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }

      console.log(x);
    }
  }
}

const Rec = new Rectangle(2, 3);
Rec.print();
