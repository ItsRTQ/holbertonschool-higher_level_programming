const target = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json)
    .then(apiData => {
        const titleDict = apiData['results'];
        for (let i = 0; i < titleDict.length; i++) {
          //Se Crea el elemento con el nombre del titulo
        }
    })