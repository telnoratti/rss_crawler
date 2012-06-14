#!/usr/bin/python3
import sys
from urllib.parse import unquote
from urllib.parse import urlparse

isodict = {}

def replacenames():
    for line in sys.stdin.readlines():
        line = line.rsplit(',', 1)
        line[1] = isodict[unquote(line[1].strip().lower())]
        print(','.join(line))

def formatiso():
    for line in open('../../isocodes.csv').readlines():
        line = line.rsplit(',', 1)
#        print(unquote(line[0].lower()))
        isodict[line[0].lower()] = line[1].strip()

def formatcsv():
    for line in sys.stdin.readlines():
        line = line.rsplit(',', 1)
        url = urlparse(line[0])
        line.insert('://'.join([url.scheme, url.netloc.rsplit(':', 1)[0]]), 0)
        line[0


if __name__ == '__main__':
#    formatiso()
#    replacenames()
