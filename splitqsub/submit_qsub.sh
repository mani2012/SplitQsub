#!/bin/bash
for filename in ./*.qsub; do
    qsub "$filename"
done
