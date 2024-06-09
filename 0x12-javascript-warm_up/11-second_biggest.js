#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments */
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
console.log(args.length > 1 ? args[1] : 0);
