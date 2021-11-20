"""
Autor: Voitov Vladimir
Date: 16.11.2021
Task: Class Work for L3
"""
m1 = [] # empty list
agn = int(input('How many numbers u want? ')) # input a number of iterations
for c in range(agn): # loop for input elem in list
    num = int(input('Input a number: '))
    m1.append(num)
m1.sort() # sort greater -> lower
print('Sorted list: ',m1)
m1.reverse() # sort lower -> greater
print('Revesed list: ', m1)
"""
Same but with letters
"""

m2 = [] # empty list
agn = int(input('How many letters u want? ')) # input a number of iterations
for d in range(agn): # loop for input elem in list
    let = (input('Input a letter: '))
    m2.append(let)
m2.sort() # sort greater -> lower
print('Sorted list: ',m2)
m2.reverse() # sort lower -> greater
print('Revesed list: ', m2)
"""
Slices
"""
m3 = m1[:3]+m2[3:]
print('m3 = m1[:3]+m2[3:] =',m3) # conc
m4 = m3[:]
print('m4 = m3[:] = ',m4) # copy elem
del m4[:] # clear list
print('m4 after del: ',m4)
"""
operators the 'in' and 'not in'
"""
m5 = []
count = 0 
for char in m1:
    if char not in m3:
        count += 1
        m5.append(char)
print('m5 = ', m5, 'and count = ', count)
