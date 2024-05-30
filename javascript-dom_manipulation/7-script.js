const target = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(apiData => {
    const titleDict = apiData.results;
    for (let i = 0; i < titleDict.length; i++) {
      const toAddElement = document.createTextNode(titleDict[i].title);
      const titleToAdd = document.createElement('li');
      titleToAdd.appendChild(toAddElement);
      target.appendChild(titleToAdd);
    }
  })
  .catch(error => console.log(error));
