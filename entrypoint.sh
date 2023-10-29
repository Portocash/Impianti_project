#!/bin/bash

FILENAME="results/2550_3_dk.csv"

vmstat 1 300 | awk '{if (NR>2) { "date +\"%Y-%m-%d %H:%M:%S\"" | getline timestamp; print timestamp "," $0; } }' | tr -s ' ' ',' > "$FILENAME" &

/usr/sbin/apache2ctl -D FOREGROUND

