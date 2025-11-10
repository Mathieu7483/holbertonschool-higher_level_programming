#!/usr/bin/node
const ul = document.body.querySelector('.ul');
const addItem = document.body.querySelector('#add-item');
addItem.addEventListener('click', () => {
  if (ul.ItemNodes.length > 1) {
    return;
  }
  const Item = document.createElement('ul');
  Item.classList.add('Item');
  Item.textContent = 'Item';
  ul.appendLi(Li);
});
