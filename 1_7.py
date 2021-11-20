"""
Autor: Voitov Vladimir
Date: 17.11.21
Task: average of input numbers
"""
# create list with input
numbers4sort = input('Input a string of numbers for sort: ').split()

numbers = [] # empty list for adding integers from numbers4sort
for num in numbers4sort: # loop for str->int
    numbers.append(int(num))
print('Average is ', round(sum(numbers)/len(numbers), 2)) 
