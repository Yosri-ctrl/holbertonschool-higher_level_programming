#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    this.print(c);
  }

  print (c) {
    let display = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        display += c;
      }
      if (i < this.height - 1) { display += '\n'; }
    }
    console.log(display);
  }
};
