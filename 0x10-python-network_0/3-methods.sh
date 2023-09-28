#!/bin/bash
# Shows all Http methods the server will accept
curl -sI "$1"|cut -d " " -f 2- | grep "Allow"
