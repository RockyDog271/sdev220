# importing tool/lib 's
from random import randint

# Input
guess = int(input("Guess the secret number (1 - 10): "))
secret = randint(1, 10)

# Logic (runs once, didn't say use a loop :/ )
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")    

'''
Required: randnum = "secret"
Required: use if/else/elif
Required: use "too low" and "too high" and "just right"
Required: use var "guess"
'''