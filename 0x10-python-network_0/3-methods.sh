#!/bin/bash
# A script that displays all HTTP methods a server will accept
curl -s -i -X OPTIONS "$1" | grep "Allow:" | sed 's/Allow: //'
