#!/bin/bash

cat $1 | awk '!/^[[:blank:]]*$/' | awk '$0 !~ /id_0 for no gain/' | awk '$0 !~ /id_ for no gain/' > $2
#This is a script to clean up some of the hardcounts, muffed punts, and other oddities remaining in the data.