#!/usr/bin/python3
import requests
import re
import sys


pat = re.compile(r'<a *class="offsite" *href="([^"]+)">')

def main():

    country = sys.argv[1]
    i = 1
    results = True
    while (results):
        raw = requests.get(''.join(['http://technorati.com/search?return=sites&authority=all&q=',country,'&page=',str(i)])).text

        results = pat.findall(raw)
        for r in results:
            if r != 'None':
                print(','.join([r,country]))
        i += 1
        print(str(i), file=sys.stderr)


if __name__=='__main__':
    main()
