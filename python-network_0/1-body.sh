#!/bin/bash
# Sends a GET request and displays body only if HTTP response is 200
curl -s -o /tmp/curl_body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/curl_body
