word = 'Spathiphyllum' # word that we need
print('Please enter a plant') # ask for enter a word
user_word = input() # user input
# start a comparison
if word == user_word:
    print('Yes - Spathiphyllum is the best plant ever!')
elif word.lower() == user_word:
    print('No, I want a big Spathiphyllum!')
else:
    print('Spathiphyllum! Not', user_word, '!')