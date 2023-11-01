const _Uri = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $movieList = $('ul#list_movies');
$.ajax({
  url: _Uri,
  dataType: 'json'
}).done((data) => {
  const _movie = data.results;
  for (let i = 0; i < _movie.length; ++i) {
    const movieTitle = _movie[i].title;
    const element = `<li>${movieTitle}`;
    $movieList.append(element);
  }
});
