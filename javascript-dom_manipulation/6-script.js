const target = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (apiData) {
    target.textContent = apiData.name;
  })
  .catch(function (error) {
    console.error('Error', error);
  });
