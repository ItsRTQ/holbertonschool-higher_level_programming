const target = document.getElementsByClassName('my_list')[0];
const addItemButton = document.getElementById('add_item');
addItemButton.onclick = function() {
  const itemToAdd = document.createElement('li');
  const text = document.createTextNode('Item');
  itemToAdd.appendChild(text);
  target.appendChild(itemToAdd);
}
