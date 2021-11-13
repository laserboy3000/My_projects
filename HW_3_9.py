vowels = 'aeio' # vowels
user_word = input('please enter a word: ') # ask user for input a word 
for k in user_word: # start a loop
    if k in vowels:
        continue
    else:
        print(k)