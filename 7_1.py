############################
# Autor: Voitov Vladimir   #
# Date: 29.11.21           #
# Task: Home WOrk to L7    #
############################
'''create split()'''


def mysplit(blabla, space = ' '): # func with 2 arg(string, default value)
    if blabla.count(' ') == len(blabla): # if string is only spaces or empty string
        new_str = []
    elif space in blabla: # if string include spaces
        blabla = blabla.lstrip() # del spaces from left side
        blabla = blabla.rstrip() # del spaces from right side
        new_str = [] # create new list
        st_sl = 0 # start index
        while True: # start loop
            found = blabla.find(space, st_sl) # found 1st space in the string
            if found == -1: # if no spaces .find() = -1
                new_str.append(blabla[st_sl:]) # all astring adding to the list
                break # stop 
            new_str.append(blabla[st_sl:found]) # adding slices from 0/space to next space
            st_sl = found +1 # next start index this is previosly index +1(to skip space)
    
    else: 
        return blabla
    return new_str # return finish list

'''Examples'''

print(mysplit('  '))
print(mysplit('Q W E R T Y  '))
print(mysplit('  Q W E R T Y'))
print(mysplit('Q W E R T Y  0123, 45: 456'))
