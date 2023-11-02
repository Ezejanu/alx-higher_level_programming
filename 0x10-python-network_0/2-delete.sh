#!/bin/bash
# Sends a DELETE request to the URL passed and displays the body of response
echo $(curl -X DELETE -s "$1")
