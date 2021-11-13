print('Guess the magician\'s secret number, muggle!!!') # Greating
cor_num = 7 # correct secret number
num = int(input()) # input from muggle
while num != cor_num: # start the magic
    print('Ha ha! You\'re stuck in my loop!') # output if not guess
    num = int(input()) # another input
print('Well done, muggle! You are free now.') # output if guess
print()
print('another task with _for_')
for i in range(17, 50, 1):
    if i ==35:
        print(i)
        print('yeap')
        break
    else:
        print(i, 'not that')