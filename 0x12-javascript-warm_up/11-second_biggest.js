#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0)
} else {
    let a = process.argv.slice(2)
    const second = a.sort((a, b) => b - a)[1];
    console.log(second);
}