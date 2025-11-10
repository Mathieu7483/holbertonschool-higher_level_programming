#!/usr/bin/node

const translateElement = document.getElementById('hello');
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(response => response.json())
  .then(data => {
    translateElement.textContent = data.hello;
  });
