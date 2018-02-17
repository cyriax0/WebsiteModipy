#!/usr/bin/env python2
'''watches a website and alarams when it is modified.'''

import sys
import urllib2
import hashlib

def main(url):

    page = urllib2.urlopen(url)
    content = page.read()
    page.close()
    # Reads the page.

    initial_hash = hashlib.md5()
    initial_hash.update(content)
    initial_hash = initial_hash.digest()
    # Hashes the content.

    print(initial_hash)
    # Prints for debugging pruposes.
    # TODO remove

if __name__ == '__main__':
    main(url=sys.argv[1])
    # Url will be passed as console argument. I.e.: 'https://www.foo.bar', 'file:///path/to/file/foo.html'
