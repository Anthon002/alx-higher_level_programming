const _Uri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $_divCharacter = $('div#character');
$.ajax({
  url: _Uri,
  dataType: 'json'
}).done((data) => {
  $_divCharacter.text(data.name);
});
