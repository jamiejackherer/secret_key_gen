#!/usr/bin/python3.6

import random
from random import shuffle
def mkkey(length):
    stuff = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM;#:@~/<>?!£$%^&*()[]{}'
    s = []
    for i in range(length):
        s.append(random.choice(stuff))
    key = shuffle(s)
    key = ''.join(s)

    print(key)
    
    return key
    
    
if __name__ == '__main__':
    mkkey(128)
