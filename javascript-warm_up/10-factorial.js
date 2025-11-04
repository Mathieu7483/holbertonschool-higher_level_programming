#!/usr/bin/node
function fact (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
const [, , argValue] = process.argv;
const number = parseInt(argValue);
console.log(fact(number));
