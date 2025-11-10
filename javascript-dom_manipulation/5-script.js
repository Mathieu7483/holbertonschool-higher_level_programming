#!/usr/bin/node
document.querySelector('#update_header').addEventListener('click', function () {
  const updateHeader = document.createElement('header');
  newItem.textContent = 'New Header!!!';
  document.querySelector('.update_header').appendChild(updateHeader);
});
