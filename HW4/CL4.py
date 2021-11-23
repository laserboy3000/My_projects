"""
Autor: Voitov Vladimir
Date: 17.11.2021
Task: Class work
"""
# 1st function
def message(): # create a function that ask for input from user and output it
    print('Enter a value: ')
    a = input()
    print(a)

print('We start here.')
message() # call the function
print('We end here.')
# 2nd func with parameter
def message2(number): # create a function with parametr
    print('Enter a number: ', number)

a = int(input('variable out of function : '))
message2(56)
print(a)

"""
function with 2 values
"""
def message2(what, number):
    print('Enter', what, 'number', number)

# invoke the function
a = 'NANANANA'
#examples
message2(a, '333')
message2('telephone', 11)
message2('price', 5)
message2('number', 'shnumber')

"""
Position parameter passing
"""
def my_func(a, b, c = 777): # 3 values include
    print(a, b, c)

my_func(1, 2, 4)
my_func(1, 2)
my_func(3, c = 1, b = 2)
# my_func(12, a = 98, b = 2)  output: error multiple values for arg 'a'

def introduction(first_name = 'Sidor', sec_name = 'Applov'):
    print('Hello, my name is', first_name, sec_name)

introduction('Ivan') 
introduction('Ivan', 'Petrov')
introduction('Petrov', 'Ivan')
# swap values
introduction(sec_name = 'Ivanov', first_name = 'Petr')
introduction(sec_name = 'Borisov')

# with variables values
frst = 'ALLA'
scnd = 'LAAL'

introduction(frst, scnd)
