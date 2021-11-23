"""
Autor: Voitov Vladimir
Date: 16.11.2021
Task: Class Work for L3
"""
# create empty list
numbers = []
# loop for input  from user for append in the list
for i in range(5):
    numbers.append(int(input('Input a number: ')))  # str -> int append numbers
print('numbers: ', numbers)
# change numbers with index
numbers[3] = 777 
print('new_numbers', numbers)
numbers[0], numbers[3] = numbers[3], numbers[0]
print('a,b = b, a', numbers)
numbers[2] = numbers[0]
print('last numbers', numbers)
# len lst
print('len "numbers": ', len(numbers)) 
# del element by index
del numbers[-1]
print('list: ', numbers, 'last elem: ', numbers[-1], 'first elem: ', numbers[0], sep = '\n')
print('*'*10)
# del spaces
str1 = ' jjjJJJ3 4 5   '
print(str1, 'len string: ', len(str1))
str1 = str1.rstrip()
print(str1, 'len string: ', len(str1))
str1 = str1.strip()
print(str1, 'len string: ', len(str1))
print('*'*10)
# append(), insert(x, y)
print('Adding elemets')
s = ['q', 'e', 'r', 't']
print(s)
s.append('y')
s.insert(1, 'w')
print(s)
print('*'*10)
# creating the list with input()
print('Creating the list of numbers by input from user, total of numbers')
my_list = []
total = 0
for i in range(9): 
    my_list.append(i**i)
    print(my_list)
    print('len = ', len(my_list))
    total += my_list[i]
print('total:',total, 'my_list:', my_list, sep = '\n')
# Bubble sort

my_list = [6, 5 , 9, 11, 23, -5, 0, 59]
Flag = True

while Flag:
    Flag = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            Flag = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            
print(my_list)
"""
OPERATORS 'in' and 'not in'
"""
num_list = [19, 0, 5, 78, 9, 23, 555, 777, 35]
print(4 in num_list)
print(4 not in num_list)
print(0 in num_list)

largest = num_list[0] # start variable

for q in num_list[1:]: # loop for find largest number
    if q > largest:
        largest = q
print(largest)
# loop for find elem index and counter
to_find = 23
found = False
count_num_list = 0

for m in range(len(num_list)):
    found = num_list[m] == to_find
    count_num_list += 1
    if found:
        break
if found:
    print('Element found at index ', i, '. we did ', count_num_list, 'trying!')
else:
    print('water')

"""
Three-dimensional arrays
"""

rooms = [[[0 for i in range(20)] for f in range(15)]for t in range(3)]
print('rooms: ', rooms)
rooms[1][9][13] = 1
rooms[0][4][1] = 0
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print('vacancy: ',vacancy)
print('rooms: ',rooms[1][9])
