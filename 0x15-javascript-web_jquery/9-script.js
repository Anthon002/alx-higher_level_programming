$(document).ready(function () {
  const _Uri = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $_div_Hello = $('div#hello');
  function salute () {
    return $.get({
      url: _Uri,
      dataType: 'json'
    });
  }
  salute().then((res) => {
    $_div_Hello.text(res.hello);
  });
});
