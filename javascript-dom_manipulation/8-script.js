(function () {
  function fetchAndDisplayHello () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json())
      .then(apiData => {
        const helloTxt = document.getElementById('hello');
        if (helloTxt) {
          helloTxt.textContent = apiData.hello;
        }
      })
      .catch(error => console.error('Error fetching translation:', error));
  }
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    fetchAndDisplayHello();
  } else {
    document.addEventListener('DOMContentLoaded', fetchAndDisplayHello);
  }
})();
