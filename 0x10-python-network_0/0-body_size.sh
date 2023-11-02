#!/bin/bash
# A script that displays the size (bytes) of the body of the response from a URL
echo $(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')
