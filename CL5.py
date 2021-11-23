######################################
#Autor: Voitov Vladimir              #  
#Date: 22.11.21                      #
#Task: Class work                    #
######################################

''' Functions and scopes. Class work. '''

def scope_test(): # function don't return anything
    x = 123

for i in range(3): # loop for output counter in range 0->2]
    print(i)

print(i) # output last i
scope_test() # no output 
# print(x) will be NameError
print('', '', sep = '\n')
def my_function(): # function return variable that inside in function
    var = 222
    print('Do I know that variable????', var)

var = 1 # variable outside function
my_function() # don't change vaiable outside function
print(var) # return 1

def f(): # function without variable
    print('Do I know that variable?!!!!!', var)

var = 100
print(var)
print('!!!!!', f()) # coz no variable inside
print('', '', sep = '\n')
""" Using global."""
print('Using global.', '', sep = '\n')
def my_fu(): # function change variable 'var' AFTER calling
    global var # change variable 'var' 
    var = 777
    print('Do I know that variable?', var)
    print('I got', var)
    var += 334
    print('I have', var)

var = 1
my_fu() # change varible
print(var) # output 1111
print()
###################
print('Change and del arguments.', '', sep = '\n')
def my_funct(my_list1): # function for change arguments
    print('Print #1:', my_list1)
    print('Print #2:', my_list2)
    my_list1 = [0, 1] # change arguments
    print('Print #3:', my_list1)
    print('Print #4:', my_list2)
    del my_list1[0] # del first([0]) argument in list
    print('Print #5, with del 1st arg:', my_list1)

my_list2 = [2, 3] 
my_funct(my_list2) # change arguments in my_list1, that only insside function
print('Print #6:', my_list2)
print()
'''Math key in function.'''
print('Math key in function.', '', sep = '\n')

x = 2 # variable outside function

def mult_by_var(x): 
    variab = 7
    return x * variab # variable 'x' exists only inside a function 

print('x * variab = ',mult_by_var(7)) # 7 * 7 = 49

def mult_adding(x): # here we nave a function with 1 argument(x) from user
    var = 7
    return 'adding', x + var, 'mult', x * var

print(mult_adding(4)) # 4 + 7 = 11 , 4 * 7 = 28
print(' print(variab) # NameError, coz variable only in function.')
print()
variab = 11 # call the variable
print('variab = ',variab) # output variable

def return_var(): # function for change variable(variab)
    global variab # change variable
    variab = 22 # new value
    return variab

print('Return variab global in function: ', return_var()) # example
print('Return variab: ', variab) # example
'''Simple functions: evaluating the BMI.'''
print('Simple functions: evaluating the BMI.', '', sep = '\n')

def bmi(weight, height): # function for finding body mass index
    if weight or height <= 0: # wrong condition, will be a "True" all time
        return None
    return weight / height ** 2

print(bmi(0, 0)) #None
print(bmi(4 ,4)) #None
print(bmi(-99, 1.65)) #None

def bmi(weight, height):
    # correct condition for finding body mass index
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return 'Ur bmi is: ', round(weight / height ** 2, 1)

print(bmi(352.5, 1.65))
print(bmi(120, 1.8))
print()
""" function triangle"""
print("Function triangle")
print()
def is_triangle(a, b, c): # function with 3 arguments for check is it triangle
    return a + b > c and b + c > a and c + a > b # return True or Flase

a = float(input('Enter the first side\'s lenght : '))
b = float(input('Enter the second side\'s lenght : '))
c = float(input('Enter the third side\'s lenght : '))

if is_triangle(a, b, c): # loop for check a triangle
    print('Yes it can be a triangle.') # if True
else:
    print('No, it can\'t be a triangle.') # if False
print()
'''Pythagorean theorem'''
def is_a_right_triangle(a, b, c): # function for check Pythagorean theorem
    if not is_triangle(a, b, c): # function for check is it triangle, if 'not False'
        return False
    if c > a and c > b: # if True
        return c **2 == a ** 2 + b **2 # True/False
    if a > b and a > c: # if True
        return a ** 2 == b ** 2 + c ** 2 # True/False
''' Heron formula '''
print('Heron')
def heron(a, b, c): # function for find 'S' of triangle
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c): # + check for triangle
    if not is_triangle(a, b ,c):
        return None
    return heron(a, b, c)

print('area of triangle = ',area_of_triangle(1., 1., 2. ** .5))
