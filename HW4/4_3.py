#########################################
#Autor: Voitov Vladimir                 #  
#Date: 21.11.21                         #
#Task: Year leep how many days in month #
#########################################

def what_year_days_in_month(year, month): # function for leap year
    #year = int(input('Whar year u want to know? ')) # input from user
    #month = int(input('What month u want to know? ')) 
    if year%4==0 and year%100!=0 or year%400==0: # loop for finding answer
        answ = 'This year is leap' # if year leep
    else:
        answ = 'Not leap' # if iy isn't
    if month==2 and answ == 'Not leap':
        answ2 = '28'
    elif month==2 and answ == 'This year is leap':
        answ2 = '29'
    elif month==4 or month==6 or month==9 or month==11:
        answ2 = '30'
    else:
        answ2 = '31'
    return answ, answ2 # return answer 

print(what_year_days_in_month(2000, 2))
