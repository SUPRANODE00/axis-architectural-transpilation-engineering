#!/usr/bin/env bash
OUT="docs/api/index.md"
echo "# AXIS API Reference" > $OUT
echo "" >> $OUT

find src labs -name "*.py" | while read file; do
    module=$(echo "$file" | sed 's/\//./g' | sed 's/.py$//')
    echo "## Module: $module" >> $OUT
    echo "" >> $OUT

    awk '
    /^class / { print "### Class: " $2 >> out }
    /^def /   { print "#### Function: " $1 >> out }
    ' out="$OUT" "$file"

    echo "" >> $OUT
done
