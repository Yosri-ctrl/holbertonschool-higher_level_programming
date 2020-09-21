#!/usr/bin/node

const { list } = require("./100-data");

let result = list.map((x, i) => x * i);
console.log(result);