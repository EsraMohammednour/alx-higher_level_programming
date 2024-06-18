#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 1) {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
