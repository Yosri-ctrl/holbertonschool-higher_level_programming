#!/usr/bin/node

const { list } = require('./100-data');

const result = list.map((x, i) => x * i);
console.log(list);
console.log(result);
