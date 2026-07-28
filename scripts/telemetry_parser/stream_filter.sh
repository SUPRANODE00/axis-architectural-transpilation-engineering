#!/bin/bash
# Extract and format active node signals
cat sovereign_telemetry.db | sed 's/[[:space:]]\+/ /g' | awk '$3 > 0 {print "Active Node: " $1 " [Metrics: " $3 "]"}'
