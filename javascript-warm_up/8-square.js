#!/usr/bin/node
const [, , sizeArg] = process.argv;
const size = parseInt(sizeArg);
const square = 'X';

if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';

    for (let j = 0; j < size; j++) {
      line += square;
    }

    console.log(line);
  }
}
