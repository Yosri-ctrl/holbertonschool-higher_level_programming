#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
