"""
Autor: Voitov Vladimir
Date: 17.11.21
Task: split()
"""
li1 = input('Input a string of numbers: ').split() # ask for input and adding in li1
print(li1) # output li1
numbers = [] # create new empty list
for num in li1: # loop for transformation in integers
    numbers.append(int(num))
print(sum(numbers)) # output sum numbers
