#!/bin/bash

# Script to package a Python project using zipapp with arguments

# Check if sufficient arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <source_directory> <output_file>"
    echo "Example: $0 bruteforce brute_force.py main:main"
    exit 1
fi

# Assign command-line arguments to variables
SOURCE_DIR="$1"
OUTPUT_FILE="$2"

# Run the zipapp command
python3 -m zipapp "$SOURCE_DIR" -o "$OUTPUT_FILE" -m "main:main"

# Check if the command succeeded
if [ $? -eq 0 ]; then
    echo "Archive created successfully: $OUTPUT_FILE"
else
    echo "Failed to create archive."
fi
