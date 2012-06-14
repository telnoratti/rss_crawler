#!/usr/bin/python2
from urlparse import urlparse
import sys

f = open(sys.argv[1], 'r')

for line in f:
    print(urlparse(line.split(',')[0]).netloc)
