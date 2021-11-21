#########################
#Autor: Voitov Vladimir # 
#Date: 21.11.21         #
#Task: Year leep        #
#########################

def what_year(): # function for leap year
    year = int(input('Whar year u want to know? ')) # input from user
    if year%4==0 and year%100!=0 or year%400==0: # loop for finding answer
        answ = 'YES' # if year leep
    else:
        answ = 'NO' # if iy isn't
    return answ # return answer

print(what_year())
