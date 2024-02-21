#!/usr/bin/node
const request = require('request');
const film_id = process.argv[2]
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
request(API_URL + film_id, function (err, response, body) {
  if (err) {
   console.log(err);
  } else if (response.statusCode === 200) {
    const my_response = JSON.parse(body);
    console.log(my_response.title)
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
