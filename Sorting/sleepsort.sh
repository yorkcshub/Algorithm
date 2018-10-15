#!/bin/bash
sort() {
    sleep "$1"
    echo "$1"
}
while [ -n "$1" ]
do
    sort "$1" &
    shift
done
wait

# Usage: sh sleepsort.sh [array of non-negative numbers]