###########################
# Autor: Voitov Vladimir  #
# Date: 30.11.21          # 
# Task: Class Work to L8  #
###########################

''' Exception's '''

try:
    y = 1 / 0
except ZeroDivisionError:
    print('Ooooops...')

print('THE END.')
print()

try:
    y = 1 / 0
except ZeroDivisionError:
    print('Zero Division!')
except ArithmeticError:
    print('Arithmetic problem!')

print('THE END.')
print()

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print('Arithmetic problem!')
    return None

bad_fun(0)

print('THE END.')
print()
def bad_fun1(n):
    return 1 / n

try:
    bad_fun1(0)
except ArithmeticError:
    print('What happened? An exception was raised!')

print('THE END.')
print()

''' raise '''

def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print('What happened? An error?')

print('THE END.')
print()

def bad_fun(n):
    try:
        return n / 0
    except:
        print('I did it again!')
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print('I see!')

print('THE END.')
print()

''' assert '''

import math

x = float(input('Enter a number: '))
assert x >= 0.0

x = math.sqrt(x)

print(x)
print()

try:
    print(1/0)
except ZeroDivisionError:
    print('zero')
except ArithmeticError:
    print('arith')
except:
    print('some')
print('****')

try:
    print(1/0)
except ArithmeticError:
    print('arith')
except ZeroDivisionError:
    print('zero')
except:
    print('some')
print('++++++')

def foo(x):
    assert x, 'blabla' # Flase -> stop |||| True -> continue
    return 1/x

try:
    print(foo(0))
except ZeroDivisionError:
    print('zero')
except:
    print('some')

foo(1)
print('--------')
print()

from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

assert angle % 180 != 90
print(tan(radians(angle)))
print('***********')
from time import sleep

seconds = 0

while seconds < 5:
    print('CTRL + Q, will kill them all!!')
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!!!")

print('End of 1st part')
''' 2nd part of Home Work to L8 '''

class TheSimplestClass:
    pass

my_first_bject = TheSimplestClass()

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

print('*******')

class Stack:
    def __init__(self):
        self.stack_list = []

stack_object = Stack()
print(len(stack_object.stack_list))
print('+++++++')

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()
stack_object_1 = Stack()
stack_object_2 = Stack()
#####
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
####
stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

print('Stack obj sec: ', stack_object_2.pop())
print()

class Stack:
    def __init__(self):
        self.__sstack_list = []

    def push(self, val):
        self.__sstack_list.append(val)

    def pop(self):
        val = self.__sstack_list[-1]
        del self.__sstack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

sstack_object = AddingStack()

for i in range(5):
    sstack_object.push(i)
print(sstack_object.get_sum())

for i in range(5):
    print(sstack_object.pop())

''' Continue ||| __dict__ ||| '''
print('""""""""""')
print('""""""""""')
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)

example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print('//////Class variables\\\\\\')

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()    
print(example_object_1.__dict__, example_object_1.counter)
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

print('Class variavles continued')

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print('********')
print(example_object.__dict__) #{} output?
print()

print('**********', "Cheking an attribute's existence", sep = '\n')

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(4)

print(example_object.b)
#print(example_object.a) # output AttributeError no 'a'
try:
    print(example_object.a)
except AttributeError:
    print("print(example_object.a) # output AttributeError no 'a'")
    pass

if hasattr(example_object, 'b'):
    print(example_object.b)
else: # do not output
    print('tra-ta-ta!') # do not output

print('+-+-+-+-+-+-+-+', 'hasattr()', sep = '\n')
print()
class ExampleClass1:
    attr = 1

print(hasattr(ExampleClass1, 'attr'))
print(hasattr(ExampleClass1, 'prop'))

class ExampleClass:
    a = 1
    def __ini__(self):
        self,b = 2

example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'a'))

print('Methods in detail!')
print()

class Classy:
    def __init__(self, value = None):
        self.var = value

obj_1 = Classy('object')
print(obj_1.var)
obj_1 = Classy()
print(obj_1.var)


print('setattr(), getattr()')
print()

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

