#!/bin/bash
END=100
for X in $(seq 1 $END);
do
    if [ $((X%2)) -eq 1 ]; then
        echo "$X"
    fi
done
