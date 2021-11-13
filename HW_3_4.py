# tax calculator
print('Welcome to tax calculator')
print('Please enter ur income')
for _ in range(5):
	tax = int(input())*0.15
	tax = round(tax, 2)
	print( tax, 'shekels, can be urs!!!')