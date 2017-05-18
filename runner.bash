#!/bin/bash

echo "Evaluating mean values for multiple times"

echo "rm test.txt"
rm test.txt

echo "Collecting data"
for i in {1..20}
do
    echo "iteration $i"
    python main.py | grep mean >> test.txt
done;
echo "Parsing data"

for i in {0..4}
do
    cat test.txt| grep "fun$i" | grep -Po 'mean: (\d\.\d+)' | grep -Po '(\d\.\d+)' | awk '{s+=$1} END {print "Result for '$i' ->" s}' 

done
