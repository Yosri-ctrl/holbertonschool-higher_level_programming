#!/usr/bin/node
const fs = require("fs");

fs.readFile(process.argv[2], "utf8", (err, file) => {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(file);
});
