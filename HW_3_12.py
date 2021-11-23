print('Welcome to the calculator!!!', 'for begin input "start"', 'for exit input "exit"', sep = '\n')
"""
Try to do
calculator
"""

command = input()
while command == 'start' or command == 'yes':
	
	num1 = float(input('Enter a number: '))
	operation = input('what need to do?: ')
	num2 = float(input('Enter a number: '))
	if operation == '+':
		print(round(num1+num2, 2))
	elif operation == '-':
		print(num1-num2)
	elif operation == '*':
		print(num1*num2)
	elif operation == '/':
		print(round(num1/num2, 2))
	elif operation == '**':
		print(num1**num2)
	elif operation == '//':
		print(num1//num2)
	elif operation == '%':
		print(num1%num2)
	command = input('again?')
