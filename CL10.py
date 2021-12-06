############################
# Autor: Vladimir Voitov   #
# Date: 06.12.21           #
# Task: Class Work to L10  #
############################


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)
print()
print()
class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;

object = Class(8)

for i in object:
    print(i)

print()
print()

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v, end = ' ')

print()

def power_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in power_of_2(8):
    print(v, end=' || ')
print()

t = [x for x in power_of_2(5)]
print(t)
print('','','', sep ='\n')

def fibonacci(n):
    p=pp=1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n=p+pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
print()

#create list with 3 ways
list_1 = []

for ex in range(6):
    list_1.append(10**ex)

list_2 = [10**ex for ex in range(6)]

print(list_1)
print(list_2)
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print("the_list",the_list)
#create the generator
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
print("the_generator", the_generator) # output adress

for v in the_list:
    print(v, end=" ")
print(the_list, len(the_list))
print()

for v in the_generator:
    print(v, end=" ") # output same the_list
print()
#print(len(the_generator)) no len in generator 'TypeError'
print()
print("lambda func")
print()
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')

def poly(x):
    return 2 * x**x - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)
print('same, but with lambda')
print_function([x for x in range(-2, 3)], lambda x: 2 * x**x - 4 * x + 2)
print()

print("map()")

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=" ")
print()

print("filter()")

from random import randint, seed

seed()
data = [randint(-50, 100) for x in range(5)]
filtred = list(filter(lambda x: x>0 and x%2==0, data))

print(data)
print(filtred)

print('closures')
print()
def outer(par):
    loc=par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())
print()

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

print()

def tag(tg):
    tg2 = tg
    tg2 = tg[0] +'/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner

b_tag = tag('<b>')
print(b_tag('Monty Python'))
print()

short_list = [1, 2, "Python", -1, 45, 0, 'Monty', '0.55']
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

print('using class with lambda')

class Vowels:
    def __init__(self):
        self.vow = 'aeiouy '
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]

vowels = Vowels()
for v in vowels:
    print(v, end = ' ')

print('Operations with files')
import sys

try:
    stream = open("D:\\HWs\\L10\\file.txt",  "rt", encoding = "utf-8")
    print(stream.read())
    stream.close()
except Exception as exc:
    print('Cannot open the file: ', exc)
print()
print()
from os import strerror

try:
    cnt = 0
    s = open('text.txt', 'rt')
    ch = s.read(1)
    while ch != '':
        print(ch, end ='')
        cnt +=1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file: ", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e))

print("readline()")
print()
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end ='')
            ccnt +=1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file: ", ccnt)
    print("lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e))

print()
print()
print('write()')
print()

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        s = 'line #' + str(i+1) + '\n'
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    
print()
print()
print('\nBytearrays')

data = bytearray(10)
#WRITE
for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))

#READ

data1 = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data1)
    bf.close()

    for b in data1:
        print(hex(b), end=' ')
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))

print()
print()
print('\n\nCopying files')
print()

srcname = input('Enter the source file name: ')

try:
    src = open(srcname, 'rb')
except IOError as e:
    print('Cannot open the source file: ', strerror(e.errno))
    exit(e.errno)

dstname = input('Enter the destination file name: ')

try:
    dst = open(dstname, 'wb')
except Exception as e:
    print('Cannot create the destination file: ', strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print('Cannot create the destination file: ', strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()

print('That was interesting!!!')
 
