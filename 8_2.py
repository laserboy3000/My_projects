###########################
# Autor: Voitov Vladimir  #
# Date: 30.11.21          # 
# Task: Class Work to L8  #
###########################


class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0): # constructor with 3 attr
        self.__h = hour # 1st variable
        self.__m = minute # 2nd variable
        self.__s = second  # 3d variable

    def __str__(self): # for output result
        def two_digits(val): # fuhc for int -> str
            s = str(val)
            if len(s) == 1: # if we have 
                s = '0' + s
            return s
        # another 3 variables for addind to the tuple and get it as string
        se = two_digits(self.__s)
        mi = two_digits(self.__m)
        ho = two_digits(self.__h)
        sp = [ho, mi, se]
        sp = ':'.join(sp) # string with separator as ':'
        return str(sp)


    def next_second(self):
        self.__s += 1
        
        if self.__s > 59:
            self.__s = 0
            self.__m += 1 
        
        if self.__m > 59:
            self.__m = 0
            self.__h +=1
            
        if self.__h > 23:
            self.__h = 0


    def prev_second(self):
        self.__s -= 1
        
        if self.__s < 0:
            self.__s = 59
            self.__m -= 1

        if self.__m < 0:
            self.__m = 59
            self.__h -= 1

        if self.__h < 0:
            self.__h = 23    

# Example's of calling
timer = Timer(23, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)

timer = Timer(12, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)
