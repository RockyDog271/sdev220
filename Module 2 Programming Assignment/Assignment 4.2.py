from random import randint

# Random True/False
randsmall = randint(0, 1)  # 0 for False, 1 for True
randgreen = randint(0, 1)  # 0 for False, 1 for True

# idk...
if randsmall == 1:
    if randgreen == 1:
        print("pea")
    else:
        print("cherry")
else:
    if randgreen == 1:
        print("watermelon")
    else:
        print("pumpkin")

# This seems like the easiest/laziest way but I genuinely don't know what this assignment wants :/

'''
Assign True or False to the variables small and green.
Write some if/else statements to print which of these matches
those choices: cherry, pea, watermelon, pumpkin.
'''