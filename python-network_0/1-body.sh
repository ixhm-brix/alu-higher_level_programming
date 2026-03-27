#!/bin/bash
# Sends a GET request and displays body only if HTTP response is 200
response=$(curl -s -o /tmp/curl_body -w "%{http_code}" "$1")
if [ "$response" = "200" ]; then
    cat /tmp/curl_body
fi
