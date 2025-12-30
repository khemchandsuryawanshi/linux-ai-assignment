#!/bin/bash

echo "Top CPU consuming processes:"
top -b -n1 | head -10

echo "Memory usage:"
free -m

echo "Disk IO:"
iostat -xz 1 3
