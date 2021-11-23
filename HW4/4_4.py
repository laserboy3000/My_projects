######################################
#Autor: Voitov Vladimir              #  
#Date: 21.11.21                      #
#Task: Day of the year               #
######################################

def day_of_the_year(year, month, day): # function for leap year
    #year = int(input('Whar year u want to know? ')) # input from user
    #month = int(input('What month u want to know? '))
    #day = int(input())
    
    leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    noleap_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year%4==0 and year%100!=0 or year%400==0: # loop for finding answer
        answ = 'This year is leap' # if year leep
    else:
        answ = 'Not leap' # if it isn't
    #######################################    
    if month==2 and answ == 'Not leap':
        answ2 = '28'
    elif month==2 and answ == 'This year is leap':
        answ2 = '29'
    elif month==4 or month==6 or month==9 or month==11:
        answ2 = '30'
    else:
        answ2 = '31'
    #####################################  
    if answ == 'This year is leap':
        answ3 = sum(leap_year[:month])+day
    elif answ == 'Not leap':
        answ3 = sum(noleap_year[:month])+day   
    ########################################    
    return answ3,' days in', year # return answer 

print(day_of_the_year(2000, 12, 31))

