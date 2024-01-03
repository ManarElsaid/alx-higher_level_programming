#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: ', res.statusCode);
});
