#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      const row = 'X'.repeat(this.width);
      const output = Array(this.height).fill(row).join('\n');
      console.log(output);
    }
  }
}

module.exports = Rectangle;

