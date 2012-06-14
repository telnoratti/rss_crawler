#!/usr/bin/python2.7
import requests
import re
import sys
import threading
import logging
import time

log = logging.getLogger('rss_crawl')

MAX_DEPTH = 1

NUM_THREADS = 12

rsslist = []

pat = re.compile(r'href="([^"]+)"')
pat2 = re.compile(r"href='([^']+)'")

atom = re.compile(r'<feed[^>]+xmlns="[^"]+Atom">')
rss = re.compile(r'<rss[^>]+version=')

def main():
    if len(sys.argv) != 3:
        print(''.join(["Usage: ", sys.argv[0], " <max depth> <input file>"]))
        return;
    MAX_DEPTH = int(sys.argv[1])
    f = open(sys.argv[2])
    linklist = f.readlines()

    log.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)

    counter = 0
    while len(linklist) > 0:
            try:
                url = linklist.pop()
                while counter < 3:
                    crawl_site(url)
                    counter += 1
            except:
                log.error(' '.join(['Could not crawl', url]))
            f = open("output.txt", 'w')
            f.write('\n'.join(map(','.join, rsslist)))


def crawl_site(url):
    unvisited = []
    visited = []
    line = url.split(',')
    unvisited.append((line[0], 0))
    country = "N/A"
    #print(line)

    while len(unvisited) > 0:
        url, depth = unvisited.pop()
    #    print(url)
        visited.append(url)

        log.info(''.join(['at ', str(depth), ' requesting: ', url]))

        #try:
        r = requests.get(url)
        #except:
        #    log.warn('Failed request for ' + url)

        #if len(visited) % 10 == 0:
            #print(str(len(visited)) + '/' + str(len(unvisited)))

        try:
            if atom.search(r.content):
                atomlist.append([line[0], url, 'atom', country])
                log.info(url)
            if rss.search(r.content):
                rsslist.append([line[0], url, 'atom', country])
                log.info(url)
        except:
            log.error('RSS or ATOM failed!')

        if line[0] in url and r.content and depth <= MAX_DEPTH:
            results = pat.findall(r.content, re.IGNORECASE)
            results.extend(pat2.findall(r.content, re.IGNORECASE))
###########Fix these regexes if RSS or ATOM fail e.g. no r.content
        #    print(results)
            if results:
                for result in results:
                    if not result.startswith('http'):
        #                print result
                        result = ''.join([line[0], result])
                    elif result.startswith('mailto'):
                        log.info("Found mailto: " + result)
                        continue
                    if visited.count(result) == 0 and not contains(result, unvisited):
                        log.info('Adding: ' + result)
                        unvisited.append((result, depth + 1))

def contains(url, unvisited):
    for link in unvisited:
        if url == link[0]:
            return True
    return False



if __name__ == '__main__':
    main()
