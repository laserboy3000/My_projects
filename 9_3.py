##############################
# Autor: Vladimir Voitov     #
# Date: 04.12.21             #
# Task: Weeker ||| HW to L9  #
##############################


class WeekDayError(Exception): # my error
    pass # nothing to do

class Weeker:
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun') # list of days

    def __init__(self, day): # initialization
        self.__day = day
        

    def __str__(self): # return day of the week
        if self.__day not in self.week: # if not correct input
            raise WeekDayError # call of my error
        if self.__day in self.week: # if input was correct
            return self.__day # return what day will be
            
    def add_days(self, n): # calculate day after
        k = (self.week.index(self.__day) + n)%7 # found index of day in the week
        self.__day = self.week[k] # found day with his index 
        

    def subtract_days(self, n):
        k = (self.week.index(self.__day) - n)%7 # found index of day in the week
        self.__day = self.week[k] # found day with his index

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Mondsdfay')
    print(weekday)
except WeekDayError:
    print("Sorry, I can't serve your request.")
