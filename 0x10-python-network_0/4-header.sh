#!/bin/bash
#gets arg sends GET request and displays body of the response
curl -sH "X-School-User-Id: 98" "${1}" |
