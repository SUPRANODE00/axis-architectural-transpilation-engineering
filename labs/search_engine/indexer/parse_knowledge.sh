#!/bin/bash
LOG_SOURCE="labs/witness_forensics/logs/alignment_stream.log"
INDEX_DB="labs/search_engine/db/knowledge_index.db"

# Clear existing index for clean rebuild
mkdir -p "$(dirname "$INDEX_DB")"
> "$INDEX_DB"

if [ -f "$LOG_SOURCE" ]; then
    # Parse timestamp, event, and trailing metric fields cleanly
    awk '/TERMUX_ALIGNMENT|ALIGNMENT_TRACE/ {
        timestamp = $1;
        event = $2;
        # Collect remaining fields starting from column 4 as metrics
        metrics = "";
        for(i=4; i<=NF; i++) metrics = metrics $i " ";
        print timestamp " " event " " metrics;
    }' "$LOG_SOURCE" >> "$INDEX_DB"
    echo "[INDEXER] Processed stream into shadow database."
else
    echo "[INDEXER] Stream source not found."
fi
