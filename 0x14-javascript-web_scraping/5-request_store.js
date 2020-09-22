#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
