#!/usr/bin/node
const updateElement = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateElement.addEventListener('click', () => {
  headerElement.textContent = 'New Header!!!';
});
