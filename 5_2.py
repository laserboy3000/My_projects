######################################
#Autor: Voitov Vladimir              #  
#Date: 22.11.21                      #
#Task: HW_5_2  Fibonacci numbers     #
######################################

def it_is_int(x): #check for number function
    '''Is input was a number function.'''
    try: 
        int(x) # if input was class<int> 
        return True
    except ValueError: # if not class<int>
        return False

def my_fibo(x): # fibonacci function
    x = int(x)
    f1 = f2 = 1
    f3 = 0
    for i in range(x+1):
        if i < 1:
            print('None')
        if i < 3:
            print('1')
        if i > 3:
            f3 = f1 + f2
            f1, f2 = f2, f3
            print(f3, sep = '\n')
            
print('Hello!!! Enter a number for finding a Fibonacci number!')
flag = True # label
while flag: # loop for finding with users enter a number
    x = input('Enter a number: ') # ask for enter a number
    if it_is_int(x): # check for number
        print(my_fibo(x), sep = '\n') # output a Fibonacci number
    else:
        print('Is it number... realy?', 'SHOW ME A REALY NUMBER!!!1') # input wasn't a number
    
    k = input('For exit press \ n /') # ask to continue
    if k != 'n': # if input from user not 'n', continue
        flag = True # label
    elif k == 'n': # if user input was 'n' -> exit
        print('ty, bb!!')
        flag = False
