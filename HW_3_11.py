print('Lothar Collatz, why??', 'intriguing hypothesis.', sep = '\n')
num = int(input('Please, enter a number largest than 0: '))
print(num)
while num != 1:
    if num % 2 == 0:
        num /= 2
        print(int(num))
    elif num % 2 != 0:
        num = 3*num + 1
        print(int(num))
    else:
        print('What u enter?')
print() # empty str
print('bool, 1=num', 1 == num, type(1==num)) # bool logic
print('bool, 2=num', 2 == num)
print()
if num == 1 and num !=2:
    print('Good')
print()
if num == 1 or num ==2:
    print('Good again')