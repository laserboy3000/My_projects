"""
Autor: Voitov Vladimir
Date: 17.11.21
Task: average of numbers in slice that % 3
"""
a = int(input('Input a number 1: ')) # input start
b = int(input('Input a number 2: ')) # input end
avr = [] # empty list for additions
for i in range(a, b+1): # loop for search numbers divisible by 3 
    if i % 3 == 0:
        avr.append(i)
print('numbers divisible by 3: ',avr)
print('average mean: ', round(sum(avr)/len(avr), 2))

        
