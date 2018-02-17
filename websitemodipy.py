#!/usr/bin/env python2
'''watches a website and alarams when it is modified.'''

import sys
import urllib2
import hashlib
import time
import datetime
import os

def hash_website(url):
    '''Hashes the website with the given url and returns the hash'''

    page = urllib2.urlopen(url)
    content = page.read()
    page.close()
    # Reads the page.

    hashed_website = hashlib.md5()
    hashed_website.update(content)
    hashed_website = hashed_website.digest()
    # Hashes the content.

    return hashed_website

def main(url):

    initial_hash = hash_website(url)
    print "Watching "+url

    while True:
        #time.sleep(1)
        # Checks for diffrences of the website every 10 seconds.
        
        new_hash = hash_website(url)

        if new_hash != initial_hash:
            break
        console_reset_code = ""
        if os.name == 'posix':
            console_reset_code = "\033[K\r"
        print console_reset_code + str(datetime.datetime.now()) + ' nothing changed',
        print " ",

    if os.name == 'nt':
        os.startfile('sound.mp3')
    else:
        os.system('vlc sound.mp3')
    # requieres vlc to be installed and in your path variable to work
    # in any os except windows

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(url=sys.argv[1])
    else:
        print("Checks a website for updates periodically.\n\
usage:\n\
    websitemodipy.py URL")
    # Url will be passed as console argument. I.e.: 'https://www.foo.bar', 'file:///path/to/file/foo.html'
