print('Bits!', 'input with 0 and 1, please!!', sep= '\n')
num1 = int(input('input a bits: '), 2)
print(type(num1))
num2 = ~num1
print(num2)
num3 = bin(num2)
print(num3)
print(type(num3))
num4 = int(input('input a bits:'), 2)
num5 = bin(num1&num4)
print(num5)
print()
 