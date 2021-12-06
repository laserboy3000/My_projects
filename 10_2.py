########################################
# Autor: Vladimir Voitov               #
# Date: 05.12.21                       #
# Task: HW to L10 working with files   #
########################################


# import modules
import sys 
from os import strerror

list_one = [] # create empty list

try:
    s = open('atext.txt', 'rt') # open file to read
    ch = s.read(1) # read by char
    while ch != '': # while all wil not read
        print(ch, end = '') # output chars
        ch = s.read(1)
        hc = ch
        hc = hc.lower() # get lower-case char
        list_one.append(hc) # adding lower-case chars in list
    s.close() # close file
    print()
except IOError as e:
    print("I/O error occurred: ", strerror(e))

d = {} # create dictinary

for i in range(97, 123): # loop for found chars in list
    if chr(i) in list_one:
        val = str(list_one.count(chr(i))) # get counter of keys
        key = chr(i) # get key
        d[key] = int(val) # get value for key
        print(key+'->'+val)

print(d) # out[ut dictionary
try:
    file_open = open('another2.txt', 'wt') # create and open new file to write
    # sort dictionary by values from greater to lower
    di_ct = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
    # write to the file
    for item, value  in di_ct.items():
        k = str(item+'->'+str(value)+'\n')
        file_open.write(k)
        print(item,'->', value, sep = '')

    file_open.close() # close file
    print()
except IOError as e:
    print("I/O error occurred: ", strerror(e))
 
