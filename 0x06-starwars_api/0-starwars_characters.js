#!/usr/bin/node
/* Star Wars Characters */
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js N');
}

const n = process.argv[2];

const options = {
  url: 'https://swapi.dev/api/films/' + n,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'localhost'
  }
};

let characters = null;

request(options, async (response, body) => {
  const json = JSON.parse(body);
  // let res = null;
  characters = json.characters;
  // console.log(characters);
  /* await characters.map( async (value) => {
      options.url = value;
      await request(options, (error, response, body) => {
      res = JSON.parse(body);
      console.log(res.name);
    });
    // console.log(options)
  }) */
  getCharacters(characters, 0);
});

function getCharacters (characters, index) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        getCharacters(characters, index + 1);
      }
    }
  });
}
