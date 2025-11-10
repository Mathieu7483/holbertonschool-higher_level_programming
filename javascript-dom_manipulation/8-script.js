#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      idElement.textContent = data.hello;
    });
});
