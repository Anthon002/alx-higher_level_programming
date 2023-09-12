#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  get width() {
    return this._width;
  }

  set width(w) {
    if (w > 0) {
      this._width = w;
    }
  }

  get height() {
    return this._height;
  }

  set height(h) {
    if (h > 0) {
      this._height = h;
    }
  }

  print() {
    for (let i = 0; i < this._height; i++) {
      let s = '';
      for (let j = 0; j < this._width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate() {
    [this._width, this._height] = [this._height, this._width];
  }

  double() {
    this._width *= 2;
    this._height *= 2;
  }
}

module.exports = Rectangle;

