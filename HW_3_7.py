import time # import the module

count = 1 #counter
while count!=6: # counter loop
    time.sleep(1) # time to wait before output
    print(count, ' Mississippi') #output nomber 1
    if count%2==0:
        print('---------------')
    else:
        print('***************')
    count +=1 # equal 
print() # empty string
print('Ready or not, here I come!') # final output message
print()
# another task
print('*-*-*-*-*-*-*-*-*-*-*')
largest_num = 0 # 1st variable
counter = 0 # 2nd variable

while False == False: # while True
    num = int(input('Please enter the number: ')) # ask for enter a number
    counter +=1 
    if num > largest_num:
        largest_num = num
    elif num == largest_num:
        cuntinue
    else:
        break
if counter > 0:
    print("Largest number is: ", largest_num)
    print('it took', counter, 'tries.')
else:
    print('You have not entered any number!!!!')
