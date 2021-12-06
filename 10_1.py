########################################
# Autor: Vladimir Voitov               #
# Date: 05.12.21                       #
# Task: HW to L10 working with files   #
########################################

import sys
import random
from os import strerror


try:
    fo = open('another.txt', 'wt')
    for i in range(150):
        if i % 2 ==0:
            k = random.randint(65, 90)
        else:
            k = random.randint(97, 122)
        s = chr(k)
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

list_one = []

try:
    s = open('another.txt', 'rt')
    ch = s.read(1)
    while ch != '':
        print(ch, end = '')
        ch = s.read(1)
        hc = ch
        hc = hc.lower()
        list_one.append(hc)
    s.close()
    print()
except IOError as e:
    print("I/O error occurred: ", strerror(e))
    

for i in range(97, 123):
    if chr(i) in list_one:
        print(chr(i)+'->'+str(list_one.count(chr(i))))

##############################################
##############################################
        
list_one = []

try:
    s = open('atext.txt', 'rt')
    ch = s.read(1)
    while ch != '':
        print(ch, end = '')
        ch = s.read(1)
        hc = ch
        hc = hc.lower()
        list_one.append(hc)
    s.close()
    print()
except IOError as e:
    print("I/O error occurred: ", strerror(e))

for i in range(97, 123):
    if chr(i) in list_one:
        print(chr(i)+'->'+str(list_one.count(chr(i))))
