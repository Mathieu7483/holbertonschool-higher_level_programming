#!/usr/bin/node
const args = process.argv.slice(2);
if (args.lenght < 2) {
  console.log(0);
} else {
  args.sort((a, b) => parseInt(b) - parseInt(a));
  console.log(args[1]);
}
