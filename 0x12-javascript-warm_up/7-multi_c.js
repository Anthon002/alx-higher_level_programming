#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
} else {
	let j = Number(process.argv[2]);
	let c = 0;
	while (c < j) {
		console.log('C is fun');
		c++;
	}
}
