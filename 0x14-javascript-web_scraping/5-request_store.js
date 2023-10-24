#!/usr/bin/node

const request = require('request')
const fileSys = require('fs');
request(process.argv[2]).pipe(fileSys.createWriteStream(process.argv[3]));
