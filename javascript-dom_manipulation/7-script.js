#!/usr/bin/node
const listMoviesElement = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movies => {
      const newElement = document.createElement('li');
      newElement.textContent = movies.title;
      listMoviesElement.appendChild(newElement);
    });
  });
