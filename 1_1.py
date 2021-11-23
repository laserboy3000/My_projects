numbers = [] # create empty list
for i in range(5): # loop for append numbers in list
    numbers.append(int(input('Input a number: ')))  # str -> int append numbers
print(numbers)
print('lenght of list = ', len(numbers))
k = int(input('input index in the list to del it = '))
del numbers[k] #del elem with index by user input
print('numbers now: ', numbers)
del numbers[-1] #del last elem
print('numbers without last elem: ', numbers)
