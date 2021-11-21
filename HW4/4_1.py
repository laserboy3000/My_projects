#########################
#Autor: Voitov Vladimir # 
#Date: 20.11.21         #
#Task: The calculator   #
#########################

def addition(a, b): # Operation of addition
    return a+b

def minus(a, b): # Operation of subtraction
    return a-b

def multiply(a, b): # Operation of multiply
    return a*b

def devide(a, b): # Operation of devide
    if b == 0:
        print('You can\'t divide by zero,', 'I thought you were smarter !!!', sep = '\n')
    else:    
        return a/b

def dev_ost(a, b): # Operation of division remainder 
    return a%b

def dev_celo4(a, b): # integer division
    return a//b

def expon(a, b): # Operation of exponentation
    return a**b

Flag = True # Flag for start to calculate

while Flag: # loop for calculate
    print('Hello!!!', 'This is a calculator.', sep = '\n'*2) # Greating
    print()
    print('Wonna calculate? (y/n)')
    phrase = input('Choise: ')
    if phrase == 'y':
        Flag = True
    elif phrase == 'n':
        print('Thank you, bye!')
        Flag = False
        break
    a = float(input('First number: ')) # input number fron user
    op = input('Operation: ') # input operation from user
    b = float(input('Second number: ')) # input number fron user

    print('\n')
    print('Maximum number this is: ', max(a, b))
    print('Average of two number: ', (a+b)/2)
    print()
    if op == '+':
        print(a, op, b, '=', addition(a, b))
    elif op == '-':
        print(a, op, b, '=', minus(a, b))
    elif op == '*':
        print(a, op, b, '=', multiply(a, b))
    elif op == '/':
        print(a, op, b, '=', devide(a, b))
    elif op == '%':
        print(a, op, b, '=', dev_ost(a, b))
    elif op == '//':
        print(a, op, b, '=', dev_celo4(a, b))
    elif op == '**':
        print(a, op, b, '=', expon(a, b))
    else:
        print('Something wrong')
    print()
    print('+-*/+-*/+-*/+-*/+-*/+-*/+-*/')
    print('+-*/+-*/+-*/+-*/+-*/+-*/+-*/')
    print('+-*/+-*/+-*/+-*/+-*/+-*/+-*/')
    print()
