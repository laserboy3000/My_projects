print('Please enter 4 numbers...') # ask for input from user
a, b, c, d = int(input()), float(input()), int(input()), float(input()) #users input
if a>b and a>c and a>d: # start of the comparison process 
    print("Largest of four numbers from", a, b, c, d, "is", a, type(a))
elif b>a and b>c and b>d:
    print("Largest of four numbers from", a, b, c, d, "is", b, type(b))
elif c>a and c>b and c>d:
    print("Largest of four numbers from", a, b, c, d, "is", c, type(c))
else:
    print("Largest of four numbers from", a, b, c, d, "is", d, type(d))
    print("Largest of four numbers from", a, b, c, d, "is", d, type(d))