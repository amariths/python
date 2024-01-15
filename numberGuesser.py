# level 2 project



import random
#import random module


guess = input("Type a number: ")

#checks if what user typed in is a number. because input turns value into string. this if turns into int if the what user typed is a number
if guess.isdigit():
    guess = int(guess)

    #numbers below 0 is not allowed
    if guess <= 0:
        print("please type larger than 0 next time")
        quit()

else:
    print("please type a number next time")
    quit()

#produces random number between 0 and the number user typed in
random_number = random.randint(0, guess)

#the amount of guess
guesses = 0

# user guesses the random generated number between 0 and guess. it will continue if user types in something else than number. if user types wrong it will display if user is above or below the right number. if right then it will display "you got it" with amount of guesses
while True:
    guesses += 1
    user_guess = input("guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("you were above the number! shame on you!")
    else:
        print("you were bellow the number! shame on you!")

print("you got it in", guesses, "guesses")
