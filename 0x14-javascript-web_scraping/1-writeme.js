#!/usr/bin/node

const fs = require("fs");
const filepath = process.argv[2];
const fileconten = process.argv[3];

fs.writeFile(filepath,fileconten,'utf-8',(err, data) => {
	if(err){
	console.log(err)
	}
})
