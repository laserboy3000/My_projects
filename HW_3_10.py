vowels = 'aeio' # vowels
empt_str = ''
user_word = input('please enter a word: ') # ask user for input a word 
for k in user_word: # start a loop
    if k in vowels:
        continue
    else:
        empt_str += k # using concatenation operator
print(empt_str) # output