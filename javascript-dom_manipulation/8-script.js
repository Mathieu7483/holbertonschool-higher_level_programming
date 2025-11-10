#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
  const idElement = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      idElement.textContent = data.hello;
    });
});
