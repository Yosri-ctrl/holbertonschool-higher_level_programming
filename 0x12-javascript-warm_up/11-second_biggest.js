#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const a = process.argv.slice(2);
  const second = a.sort((a, b) => b - a)[1];
  console.log(second);
}
