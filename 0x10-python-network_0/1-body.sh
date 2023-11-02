#!/bin/bash
# A script that sends a GET request to a URL, and displays body of the response
[ $(curl -s -o /dev/null -w "%{http_code}" "$1") -eq 200 ] && curl -s "$1"
