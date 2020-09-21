#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let display = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        display += 'x';
      }
      if (i < this.height - 1) { display += '\n'; }
    }
    console.log(display);
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
