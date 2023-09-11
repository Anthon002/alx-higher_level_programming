#!/usr/bin/node
function add (a, b) {
  const ans = a + b;
  console.log(ans);
}

add(Number(process.argv[2]), Number(process.argv[3]));
