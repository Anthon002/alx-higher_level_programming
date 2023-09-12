#!/usr/bin/node

class Square {
  constructor(size) {
    this.width = size;
    this.height = size;
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
