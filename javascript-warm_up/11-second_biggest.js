#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));
if (args.length < 2 || isNaN(args[0]) || isNaN(args[1])) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
