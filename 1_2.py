"""
Autor: Voitov Vladimir
Data: 16.11.21
Task: Home Work 3.2 ( append(), insert(), del
"""
# Step 1 Create empty list
beatles = []
print("Step1: ", beatles)
# Step 2 append musicians
musicians = ['John Lennon', 'Paul McCatney', 'Gearge Harrison']
for i in musicians:
    beatles.append(i)
print('Beatles №1: ', beatles)
# Step 3 append members(Stu Sutcliffe, Pete Best) with users input()
for _ in range(2):
    k = input('Input another members: ')
    beatles.append(k)
print('Beatles №3: ', beatles)
# Step 4 use the del instruction to remove Stu Sutcliffe and Pete Best
del beatles[-1]
del beatles[-1]
print('Beatles №4: ', beatles)
# Step 5 use the insert() method to add Ringo Starr to the beginning
beatles.insert(0, 'Ringo Starr')
print('Beatles №4: ', beatles)
print('SONG!!!!')
print('We all live in a yellow submarine',
      'Yellow submarine, yellow submarine',
      'We all live in a yellow submarine',
      'Yellow submarine, yellow submarine', sep='\n')
