#!/bin/bash
# Pipeline using cat, sed, and awk for telemetry parsing

cat "$1" | sed 's/[{}]//g' | awk -F',' '{print "Node:", $1, "| Value:", $2}'
