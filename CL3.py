print(r'////Class work!!!\\\\', 'Logical conditions, bool', sep = '\n') # name of work
n = int(input('Enter a number, please: '))

print('number greater than 100: ', n>100)
print('number less than 100: ', n<100)

print('is number equal 55: ', n == 55)
print('is number not equal 55: ', n != 55)

print('is number equal or greater than 100: ', n >= 100)
print('is number equal or less than 100: ', n <= 100)

print('Types') # enumeration of types 
num1 = 10
num2 = 10.0
num3 = '10.0'
print(num1, '= num1 this is', type(num1))
print(num2, '= num2 this is', type(num2))
print(num3, '= num3 this is',type(num3))

print('The if-else statement') # example the if-else statements
if n > 90 and n % 2 == 0:
    print('even number greater than 90')
else:
    print('not enought yeat')

print('The if-elif-else statement') # example the if-elif-else statements
amount = int(input(' ENter amount: '))

if amount<1000:
    discount = amount*0.05
    print('Your discount equal', discount)
elif amount<5000:
    discount = amount*0.10
    print('Your discount equal', discount)
else:
    discount = amount*0.15
    print('Your discount equal', discount)

print('Net payable:', amount-discount)
print('amount', type(amount), 'discount', type(discount))

