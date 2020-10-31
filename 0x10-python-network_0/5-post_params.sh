#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"
