const target = document.querySelector('header');
const semiButton = document.getElementById('toggle_header');
semiButton.onclick = function () {
  if (target.className === 'red') {
    target.classList.remove('red');
    target.classList.add('green');
  } else {
    target.classList.remove('green');
    target.classList.add('red');
  }
};
