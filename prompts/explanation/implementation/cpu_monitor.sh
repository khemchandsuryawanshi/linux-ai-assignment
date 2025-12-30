#!/bin/bash
echo "CPU usage:"
top -b -n1 | head -10

echo "Memory usage:"
free -m

echo "Disk IO:"
iostat -xz 1 3
