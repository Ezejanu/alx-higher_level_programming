#!/bin/bash
# Sends a DELETE request to the URL passed and displays the body of response
curl -X DELETE -s "$1"
