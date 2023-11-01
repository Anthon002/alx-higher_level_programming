const $_header = $('header');
const $update_header = $('div#update_header');
$update_header.on('click', () => {
  $_header.text('New Header!!!');
});
