#!/bin/bash
# Check database existence, then process using cat, sed, and awk
DB_FILE="sovereign_telemetry.db"

if [ ! -f "$DB_FILE" ]; then
    echo "[!] Warning: $DB_FILE not found. Initializing mock stream buffer..."
    touch "$DB_FILE"
    echo "node_alpha, 10, 1.5" >> "$DB_FILE"
    echo "node_beta, 20, 0.0" >> "$DB_FILE"
fi

cat "$DB_FILE" | sed 's/[[:space:]]\+/ /g' | awk -F',' '$3 > 0 {print "Active Node: " $1 " [Metrics: " $3 "]"}'
