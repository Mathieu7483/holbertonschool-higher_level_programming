#!/usr/bin/node
const Arguments = process.argv.length - 2;
// -2 for node exec and script path

if (Arguments === 0) {
  console.log('No argument');
} else if (Arguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
