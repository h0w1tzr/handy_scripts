#!/bin/bash
# This will take output from arp-scan and generate a list of unique IP address that were found
grep -h -P "\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" $1 | cut -f 1 | sort | uniq | tee targets
