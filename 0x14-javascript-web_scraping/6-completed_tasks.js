#!/usr/bin/node
const request = require("request");

let dic = {};
request(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  let content = JSON.parse(body);

  for (let i = 0; i < content.length; i++) {
    let user = content[i].userId;
    if (content[i].completed) {
      dic[user] = (dic[user] || 0) + 1;
    }
  }

  console.log(dic);
});
