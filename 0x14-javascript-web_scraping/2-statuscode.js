#!/usr/bin/node

const request = require("request")
const requesturl = process.argv[2]

request.get(requesturl).on('response',(response)=>{
	console.log(`code: ${response.statusCode}`)
})
