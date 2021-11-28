##################################
# Autor: Voitov Vladimir         #
# Date: 27.11.21                 #
# Task: Class Work to lection 5  #
##################################

print(' Hello, teacher!\n\
This is my class work.')

# My learn to import modules

import math as matana # rename module

def sin(x): # function for finding sin variable
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print('sin(pi/2) = ',sin(pi/2))
print('matana.sin(matana.pi/2) = ', matana.sin(matana.pi/2))
print()

# I'm learn to import function from module
print('from math import pi, e, sin ', '', sep = '\n')
from math import pi, e, sin

print('e = ', e)
print('sin(pi/2) = ', sin(pi/2))
print('pi = ', pi)
print()
print('from math import *')
from math import *

print('pi =', pi)
print('cos(170) = ', cos(170))
print()

print('from math import pi as PI, sin as SINE')
from math import pi as PI, sin as SINE

print('SINE(PI/2) = ', SINE(PI/2))

# what functions in module math
print('dir(math): ')
for name in dir(matana):
    print(name, end='\t')
print()
# selected functions from the math module
print('----+++++Mathematic======******')
from math import pi, radians, degrees, sin, cos, tan, asin
print('ad = 90.', 'ar = radians(ad)', 'ad = degrees(ar)', sep = '\n')
ad = 90
ar = radians(ad)
ad = degrees(ar)

print('ad == 90.', ad == 90)
print('ar == pi /2 = ', ar == pi /2)
print('sin(ar) / cos(ar) == tan(ar) = ', sin(ar) / cos(ar) == tan(ar))
print('asin(sin(ar)) == ar = ', asin(sin(ar)) == ar)
print()

# Selecnted function from the math modules

from math import e, exp, log
print('from math import e, exp, log')
print()
print('pow(e, 1) == exp(log(e)) = ', pow(e, 1) == exp(log(e)))
print('pow(2, 2) == exp(2 * log(2)) = ', pow(2, 2) == exp(2 * log(2)))
print('log(e, e) == exp(0) = ',log(e, e) == exp(0))

from math import ceil, floor, trunc
print('from math import cell, floor, trunc')
print()
print('x = 1.4', 'y = 2.6', sep = '\n')
x = 1.4
y = 2.6

print('floor(x) = ', floor(x), 'floor(-y) = ', floor(-y))
print('ceil(x) = ', ceil(x),'ceil(-y) = ', ceil(-y))
print('trunc(-x) = ', trunc(-x), 'trunc(y) = ', trunc(y))

# random.random()
print('random.random()')

from random import random, seed, randint
print('from random import random, seed, randint')

for i in range(5):
    print(random())
print('seed(0)', 'random() in range(5)')
seed(0)

for i in range(5):
    print(random())

print()

print('seed(10)', 'random(5)')
seed(10)

for i in range(5):
    print(random())

seed(1052, 2)

for i in range(5):
    print(random())

for i in range(10):
    print(randint(1, 10), end=',')

print('\n\n')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    print(randint(1, 10), end=',')

print('\n\n')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('for i in range(10):\n\
    print(randint(1, 10), end=",")\n\
from random import choice, sample\
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')

print('choice(my_list) = ', choice(my_list))
print('sample(my_list, 5) = ', sample(my_list, 5))
print('sample(my_list, 10) = ', sample(my_list, 10))

'''from platform import platform, machine, processor, system, version'''
from platform import platform, machine, processor, system, version

print('platform(): ', platform())
print('platform(1): ', platform(1))
print('platform(0, 1): ',platform(0, 1))
print('machine() = ', machine())
print('processor(): ', processor())
print('system(): ', system())
print('processor(): ', processor())
print()

'''from platform import python_implementation, python_version_tuple'''
from platform import python_implementation, python_version_tuple

print('python_implementation(): ',python_implementation())
print()
print('python_version_tuple')
for atr in python_version_tuple():
    print(atr, end = '.')
print()

import math
result = math.e == math.exp(1)
print('result = math.e == math.exp(1)')
print('result = ', result)
