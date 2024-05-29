const btn = document.getElementById('update_header');
const target = document.querySelector('header');
btn.onclick = function() {
  target.textContent = 'New Header!!!';
}
