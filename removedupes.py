#!/usr/bin/python2
import sys

feeds = []
o = open('clean.txt', 'w')

for line in open(sys.argv[1]):
    sline = line.split(',')
    if sline[1] not in feeds:
        feeds.append(sline[1])
        o.write(line)
