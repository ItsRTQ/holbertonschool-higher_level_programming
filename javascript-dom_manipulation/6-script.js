const target = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(apiData => target.textContent = apiData.name)
    .catch(error => console.error('Error', error));
