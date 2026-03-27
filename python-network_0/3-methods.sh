#!/bin/bash
# Displays all HTTP methods the server will accept for a given URL
curl -s -X OPTIONS -i "$1" | grep "Allow:" | cut -d' ' -f2-
