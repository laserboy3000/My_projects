###########################
# Autor: Voitov Vladimir  #
# Date: 27.11.21          #
# Task: HW 7.1            #
###########################

# Greating
print('Hello! Teacher!', "Today we will today we will get acquainted with the system", sep = '\n')
# import functions from module
from platform import platform, machine, processor, system, version, release, system_alias
import time

def plat_form(): # func for show system function
    # syst = list functions, l_syst = tuple
    syst = [platform(), machine(), processor(), system(), version(), system_alias(system, release, version)]
    l_syst = ('platform', 'machine', 'processor', 'system', 'version', 'system_alias')
    # ask for answer from user to continue
    answer = input('Hello!\n Do u want to know more? (y/n): ' )
    if answer == 'y': # if yes
        print('I can offer you the following :')
        for j in l_syst: # loop for show all of function that we import
            print(j)
    elif answer == 'n': # answer for exit from plat_form
        print('Why no?')
        exit()
    # ask for continue y or n   
    sec_answer = input('Can I show u all of them? (y/n): ')

    if sec_answer == 'y': # if 'y', we continue and go out when end the loop
        for i in range(len(syst)): # loop for call all function from the list
            for j in range(len(l_syst)):
                if i == j:
                    print(l_syst[j], ': ', syst[i]) # output
        time.sleep(0.5)
        print('bb')                  
    elif sec_answer == 'n': # if user press n
        # ask user for input
        third_answer = input('Something specific from the list? (y/n): ')
        print(l_syst) # show what he can input
        if third_answer == 'y': # continue if 'y'
            while True:  # loop for
                for_exit = input('Press any key for continue. For exit, input "stop": ')
                if for_exit != 'stop':
                    if third_answer == 'y':
                        wht = input("What exactly?: ")
                        if wht in l_syst: # check correct input
                            exac = l_syst.index(wht) # if in list
                            print(l_syst[exac] ,': ',syst[exac]) # output it 
                        else: # if input not correct
                            print('I have not it. Try another.')
                if for_exit == 'stop':
                    print('Now u know more', 'Thank you, byebye!', sep = '\n')
                    exit()
                          
        elif third_answer == 'n': # for exit
            print('What u want from me???!!?!?!', 'I have nothing more to offer you.', 'Good Bye!!!', sep = '\n')
            exit() # exit собсна

plat_form() # Start
