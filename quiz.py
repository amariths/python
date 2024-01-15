
# level 1 project

print("welcome to quiz!")


playing = input("wanna play? type yes: ").lower()

# print(playing)

# if user types yes then the game will start
# if user types something else than yes like no then the game ends
# lower() converts what the user types into lower case.
if playing != "yes" and playing != "y":
    print("have a great day!")
    quit()

print("lets play!")

# how many times user answered correct is stored in points
points = 0


#if the user types correct answer, display "correct!" and increment points for everytime user answers correct.
#otherwise it will display incorrect and not increase points.


#question 1
answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    points += 1
else:
    print("incorrect!")


#question 2
answer = input("in which country is stockholm? ").lower()
if answer == "sweden":
    print("correct!")
    points += 1
else:
    print("incorrect!")


#question 3
#some people call it football
answer = input("which sport does messi play? ").lower()
if answer == "soccer" or answer == "football":
    print("correct!")
    points += 1
else:
    print("incorrect!")


#question 4
answer = input("who was the villain in avengers endgame movie? ").lower()
if answer == "thanos":
    print("correct!")
    points += 1
else:
    print("incorrect!")



#displays "good job!" if user has more than 1 point. if its 1 point or less then it will display "dont worry"
if points > 1:
    print("you got", points, "points good job!")
else:
    print("you got", points, "point dont worry there is always next time!")
