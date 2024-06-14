#!/usr/bin/node
// star wars endpoint

const request = require('request');
if (process.argv.length > 2) {
  const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
  request(url, (err, _, body) => {
    if (err) {
      console.log('Error:', err);
    }
    const characters = JSON.parse(body).characters;
    const charNames = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (rejErr, _, resBody) => {
          if (rejErr) {
            reject(rejErr);
          }
          resolve(JSON.parse(resBody).name);
        });
      })
    );
    Promise.all(charNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
