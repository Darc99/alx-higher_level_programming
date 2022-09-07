#!/usr/bin/node
const Rectangle = require('./5-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    this.print(c);
  }
}
module.exports = Square;
