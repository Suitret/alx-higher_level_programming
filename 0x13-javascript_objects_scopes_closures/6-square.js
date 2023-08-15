#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the parent class constructor
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
