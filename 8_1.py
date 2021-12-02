###########################
# Autor: Voitov Vladimir  #
# Date: 30.11.21          #
# Task: Home Work 8.1     #
###########################

class Stack: # func for adding and delete value
    def __init__(self): # func initialization
        self.__stk = [] # create empty list

    def push(self, val): # func for adding value in list 
        self.__stk.append(val) # adding

    def pop(self): # func for del last value
        val = self.__stk[-1] # found last value
        del self.__stk[-1] # deleting last value
        return val # return value )

class CountingStack(Stack): # class with inheritance
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0 # private variable

    def get_counter(self): # func for show value of counter to the world
        return self.__counter # output counter

    def pop(self): # get pop from class Stack
        val = Stack.pop(self)
        self.__counter += 1 # adding 1 to counter


stk = CountingStack()
for i in range(100): # loop for check 
    stk.push(i)
    stk.pop()
print(stk.get_counter())
