######################################
#Autor: Voitov Vladimir              #  
#Date: 22.11.21                      #
#Task: HW_5_1     Factorial          #
######################################


def my_factorial(x): # function for finding a factorial number
    '''Factorial finding function.'''
    factor = 1 # start search
    x = int(x) # variable of number for finding
    for i in range(1, x + 1): # loop for finding
        factor *= i # factorial equation
    return factor

def it_is_int(x): #check for number function
    '''Is input was a number function.'''
    try: 
        int(x) # if input was class<int> 
        return True
    except ValueError: # if not class<int>
        return False
print('Hello!!! Enter a number for finding a factorial number!')
flag = True # label
while flag: # loop for finding with users enter a number
    x = input('Enter a number: ') # ask for enter a number
    if it_is_int(x): # check for number
        print('Factorial of', x, '=', my_factorial(x)) # output a factorial
    else:
        print('Is it number... realy?', 'SHOW ME A REALY NUMBER!!!1') # input wasn't a number
    
    k = input('For exit press \ n /') # ask to continue
    if k != 'n': # if input from user not 'n', continue
        flag = True # label
    elif k == 'n': # if user input was 'n' -> exit
        print('ty, bb!!')
        flag = False

print(my_factorial.__doc__)
print(it_is_int.__doc__)
