#!/usr/bin/node
const Arguments = process.argv;
const userinput = Arguments.slice(2);

if (!userinput[0]) {
  console.log('No argument');
} else {
  console.log(userinput.join(' '));
}
