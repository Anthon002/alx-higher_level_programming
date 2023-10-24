#!/usr/bin/node

const fs = require("fs")
const filepath = process.argv[2]

fs.readfile(filepath,'utf-8',(err,data)=>{
console.log(err||data)
})
