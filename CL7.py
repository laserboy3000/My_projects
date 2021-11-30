############################
# Autor: Voitov Vladimir   #
# Date: 29.11.21           #
# Task: Class WOrk to L7   #
############################

''' Hello Teacher!!!\
This is my class work for L7.'''

while True: # loop for except Errors
    try:
        value = int(input('Enter a natural number: '))
        print('The reciprocal of: ', value, 'is', 1/value)
        break
    except ValueError: # 123 != sdf
        print('I do not know what to do.')
    except ZeroDivisionError: # 1/0 not correct input 
        print('Division by zero is not allowed in our Universe.')
    except:
        print('What?? Something strange has happened here... Sorry!')

'''Operators on strings'''

char_1 = 'a' #variable1
char_2 = ' ' #variable2 = space

'''Unicode'''

print('ord(char_1): ', ord(char_1)) # from a table of unicode ? 
print('ord(char_2): ', ord(char_2)) 


char_greek = 945 # variable3 'alpha'

print('chr(char_greek = 945): ', chr(char_greek)) # output 'alpha'

x = 'a'
print("x = 'a'")
x1 = 97
print("x1 = 97")

print('type(x): ', type(x))
print('type(ord(x)): ', type(ord(x)))
print('type(chr(x1)): ', type(chr(x1)))

print('chr(ord(x)), x: ', chr(ord(x)), x) # output 'a a'
print('chr(ord(x)) == x: ', chr(ord(x)) == x) #bool True

'''Indexing'''

the_str = 'silly walks'

for xi in range(len(the_str)): # loop for output symbols in string 'silly walks'
    print(the_str[xi], end = ' ')

print()

for q in range(len(the_str)-1, -1, -1):# loop for reverse output symbols
    if q % 2 == 0:
        print(the_str[q], end = ' ') # space separated output
    else:
        print(the_str[q], end = '\n') # from new line
print()

'''Slices'''

new_str = "qwerty_4_ever"

print('new_str = "qwerty4ever"')
print('new_str[1:6]: ', new_str[1:6])
print('new_str[1:]: ', new_str[1:])
print('new_str[:6]: ', new_str[:6])
print('new_str[2:-5]: ', new_str[2:-5])
print('new_str[-2:5]: ', new_str[-2:5])
print('new_str[::2]: ', new_str[::2])

'''in not in'''

print("'qw' in new_str: ", 'qw' in new_str)
print("'2' in new_str: ", '2' in new_str)
print("'ever' in new_str: ", 'ever' in new_str)
print("'2' not in new_str: ", '2' not in new_str)
print("'never' not in new_str: ", 'never' not in new_str)

"""concatination"""

new_str = new_str + '_but_123_is_bettter!'
print("new_str = new_str + '_but_123_is_bettter!'")
print(new_str)



'''operation min()/max()'''

print('min(new_str): ', min(new_str))

t = 'For the Emperor!!!!' # new variable(str)
print("t = 'For the Emperor!!!!'")
print('[' + min(t) + ']') # min symbol in unicode
print('[' + max(t) + ']') # max symbol

space = min(t) # anoter variable
print("is a space:", "\"", space, "\"", sep = "")
print(ord(space)) 
print()

t = [0, 1, 2] # rename new variable(was str)
print('t = [0, 1, 2]')
print('min(t): ', min(t)) # min number in list
print('max(t): ', max(t)) # max number in list

'''Index.\
The method returns the index\
of the first occurrence\
of the argument.'''

print('blood to the Bloody God'.index('b') +1)
print('blood to the Bloody God'.index('t') +1)
print('blood to the Bloody God'.index('B') +1)
print('blood to the Bloody God'.index('G') +1)

print('list() func')

st = 'Iron Within, Iron Without'
print(st, type(st), list(st))

di = {1: '1', 2: '2'}
print(di, type(di), list(di))

print('count() metod') #counter symbols in the list()

print('blood to the Bloody God'.count('b'))
print('blood to the Bloody God'.count('o'))
print('blood to the Bloody God'.count(' '))
print()

''' capitalize() '''
# 1st symbol get upper-case if it letter other will be lower-case

print('alpha'.capitalize())
print('oMeGa'.capitalize())
print('ALPHARIUS'.capitalize())
print(' Aplha'.capitalize())
print('0101100010'.capitalize())


print('4.23 a.m.', 'there are still a few methods left.', sep = '\n')
print('Thanks you)')



