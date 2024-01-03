#!/usr/bin/node

const movieid = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log((JSON.parse(body)).title);
});
