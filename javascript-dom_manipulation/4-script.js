#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  const addItemButton = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');

  function addItem () {
    const newLi = document.createElement('li');

    newLi.textContent = 'Item';

    myList.appendChild(newLi);
  }

  if (addItemButton && myList) {
    addItemButton.addEventListener('click', addItem);
  } else {
    console.error("Elements 'add_item' ou 'my_list' not found.");
  }
});
