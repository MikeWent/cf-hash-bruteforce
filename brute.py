#!/usr/bin/env python3

import hashlib

class COLORS:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_hashes(text):
    text = text.encode('utf-8')
    md5 = "MD5: " + hashlib.md5(text).hexdigest()
    sha1 = "SHA1: " + hashlib.sha1(text).hexdigest()
    sha256 = "SHA256: " + hashlib.sha256(text).hexdigest()
    return md5, sha1, sha256

def number_generator(start, end):
    n = start
    while n <= end:
        yield n
        n += 1

PHRASE = input('Enter word to bruteforce: '+COLORS.BOLD)
print(COLORS.ENDC, end='')
RAW_CYCLES = input('Set maximum bruteforce cycles [500]: '+COLORS.BOLD)
if RAW_CYCLES == '':
    CYCLES = 500
else:
    try:
        CYCLES = int(RAW_CYCLES)
    except:
        print(COLORS.RED+'Incorrect value!'+COLORS.ENDC)
        exit()

print(COLORS.ENDC+'---')

for n in number_generator(0, 1000):
    variant = PHRASE + str(n)
    hashes = get_hashes(variant)
    for hashstr in hashes:
        if hashstr.endswith('cf'):
            print(COLORS.BOLD+COLORS.GREEN+variant+COLORS.ENDC)
            print(hashstr)
            print('---')
            
print(COLORS.BLUE+'Done!'+COLORS.ENDC)