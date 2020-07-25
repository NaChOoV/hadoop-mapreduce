#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
code = ''
for line in sys.stdin:

    data = line.strip().split()
    if len(data) == 10:
        method = data[5].replace('"','')
        code = data[8]
        
        if method == 'GET':
            if code[0] == '4':
                print "4XX\t1"

