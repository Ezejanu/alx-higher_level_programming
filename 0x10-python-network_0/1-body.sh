#!/bin/bash
# A script that sends a GET request to a URL, and displays body of the response
curl -s -o /dev/null -w "%{http_code}" -i "$1" | awk '/^200$/ {p=1; next} p'
