#!/usr/bin/env bash

inotifywait -m $1 -e close_write | # -m is --monitor, -e is --event
    while read path action file; do
	filepath="$( cd "$( dirname "$1" )" >/dev/null 2>&1 && pwd )"

	size=`du -h "$1" | cut -f1`

	my_ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')

	now=$(date -u)

        doc='{"csrfmiddlewaretoken":"932pKN7RZsPjd1s2UCzH3DoSFLSpde0IIa84iMyEh16nWw4aLrgBMqaCv0xKrg5U","filename": "'$1'","filepath": "'$filepath'","file_size": "'$size'","client_ip": "'$my_ip'","time": "'$now'"}'
		
	echo '$doc'

	command=$(curl -XPOST 'http://localhost:8000/logger/' -H 'Content-Type: application/json' -d "$doc")
	echo $command
    done
