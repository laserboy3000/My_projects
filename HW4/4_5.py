######################################
#Autor: Voitov Vladimir              #  
#Date: 21.11.21                      #
#Task: Prime number                  #
######################################


def is_prime(num): # The function
    count = 0 # counter for loop
    for i in range(1, num+1): # loop for find answer
        if num%i == 0:
            count += 1 # +1 if when num devided
    ###########################
    if count == 2: # if number is prime it have two divisors 
        k = 'Yes'
    else: # if counter != 2 answer will be not prime
        k = 'No'
    #################    
    if k == 'Yes':
        return num # if number is prime, print it

for i in range(1, 20): # loop for findins all primes number
    if is_prime(i + 1):
        print(i+1, end = ' ')

print()
