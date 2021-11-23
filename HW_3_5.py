print('What kind of year?', 'What year u want to know?', sep='\n') # Greating
year = int(input()) #ask for input 
# answer
if year%4==0 and year%100!=0 or year%400==0:
    print('Year is leap!!!')
else:
    print('Leap?', 'nope', sep='\n')
print()

"""
Next task
"""

print('example endless cycle')
print('while 1<2:', 'print(\'no, please nooooooooooooo\')', sep='\n')
print()

count = 10 # variable
while count != -1: # start cycle
    print('Ur count is: ', count)
    count -=1
print('bye bye')
print()
