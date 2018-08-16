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
    length = input('[+] Please choose a length for your new secret key\n[+] Please chose a length of 10 or more.\n>>> ')
    if int(length) <= 10:
        print('[+] Having a length of less than 10 chars is\n| not recomended so we think you need a longer one!\n| We will choose a length of 128 for you.')
        length = 128
    mkkey(int(length))
