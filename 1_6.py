"""
Autor: Voitov Vladimir
Date: 17.11.21
Task: Write a program that takes as input a list of
numbers on one line and displays on one line the
values ​​that appear more than once in it.
"""
# create list with input
numbers4sort = input('Input a string of numbers for sort: ').split()

numbers = [] # empty list for adding integers from numbers4sort
for num in numbers4sort: # loop for str->int
    numbers.append(int(num))
print(numbers)

count = 0 # counter
uni = [] # empty list of repetitive readings

for k in range(len(numbers)-1): # loop for search and addition in uni list
    for j in numbers[k+1:]:
        if numbers[k] == j:
            count +=1
            if count >=1:
                if numbers[k] not in uni:
                    uni.append(numbers[k])
print('uni: ', uni) # output list of repetitive readings 
uni.sort()
print('sorted uni: ', uni) # output sorted list of repetitive readings 
                
