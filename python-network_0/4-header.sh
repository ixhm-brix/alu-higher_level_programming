#!/bin/bash
# Sends a GET request with header X-HolbertonSchool-User-Id set to 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "http://$1"
