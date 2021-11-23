"""
Autor: Voitov Vladimir
Date: 16.11.2021
Task: Unique 'in' and 'not in' HW3.4 L3
"""
#list of numbers and letters
exmpl = [1, 3, 5, 7, 3, 1, 10, 9, 'A', 'a', 'B', 'B', 6, 8, 10, 9] 
uni = [] # list for unique symbols
n = len(exmpl)
for i in range(n):
    if exmpl[i] not in exmpl[i+1:]:
        uni.append(exmpl[i])
print('uni = ',uni)
# list for <<class int>> only
uni2 = []
for k in uni:
    if type(k) == int:
        uni2.append(k)
print('uni2 = ',uni2)
# list 4 <<class str>> only
uni3 = [j for j in uni if j not in uni2]
print('uni3 = ',uni3)
# list 5 with split by
uni4 = [i for i in input('input a string: ').split()]
print('uni4 = ', uni4)
"""
Multidimensional nature of lists:
advanced applications
"""

temps = [[h*d*0.5 for h in range(1, 25)] for d in range(1, 32)]
#
# some kind of magic
#
total = 0.0
for day in temps:
    total += day[11]

average = total / 31

highest = -10
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
            

print('Average temperature at noon: ', average, 'F.')
print('The highest temperature was: ', highest, 'F.')
