#!/usr/bin/node
document.querySelector('#update_header').addEventListener('click', function () {
  const updateHeader = document.createElement('header');
  newHeader.textContent = 'New Header!!!';
  document.querySelector('.update_header').appendChild(updateHeader);
});
