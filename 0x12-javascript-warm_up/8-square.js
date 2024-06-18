#!/usr/bin/node
const args = process.argv.slice(2);
const number = parseInt(args[0]);

if (!isNaN(number) && args.length === 1) {
  for (let i = 0; i < number; i++) {
    let line = '';
    for (let s = 0; s < number; s++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
