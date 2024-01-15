# level 3 project


import random

user_wins = 0
computer_wins = 0
move = ["rock", "paper", "scissors"]

while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in move:
        continue

    random_number = random.randint(0, 2)

    computer_pick = move[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    else:
        print("You lost! shame on you!")
        computer_wins += 1

print("you won", user_wins, "times.")
print("computer won", computer_wins, "times.")
print("bye")
