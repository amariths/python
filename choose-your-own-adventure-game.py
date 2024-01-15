# level 4 project


name = input("type your name: ")
print("welcome", name, "to this adventure")

answer = input("\n your village is in a fierce battle. you have combat skills but the battle is too dangerous. your only choice is to find a way out of the village and escape with your friends. there are 2 paths, the safer one and the danger one. which would you like to go? type safe or danger " ).lower()

if answer == "safe":
    answer = input("\n the path seems safe. you and your friends are safe for now. you come across a path where it leads to escape quickly but it has dangerous magic spells and explosions. there is another path that is longer but is safer. which would you choose? type safe or danger ")

    if answer == "danger":
        print("\n you and your friends got hit by magic spells and died")
    elif answer == "safe":
        answer = input("\n you and your friends are on a safe path and finding a way. its taking time but at least your safe. youre almost there but you and your friends are hungry and tired so you have no choice but to rest. you can continue to escape but with low energy you wont make it. or you can look for food and has higher chance of surviving. what will you do? type continue or loot: " )
        if answer == "continue":
            print("\n you and your friend did not reach escape fast enough and got hit by magic spells and died")
        elif answer == "loot":
            answer = input("\n you and one of your friends went to look for food. you find a building that has alot of loots. you come across a weak level monster. there are food everywhere but not enough. but the place that has alot of food is blocked by the monster. will you fight it or loot safely? type safe or fight " )
            if answer == "safe":
                print("\n you find some food but its not enough. you continue to escape with friends but some of you got hit and died and you and your remaining friends survived.")
            elif answer == "fight":
                print("\n you end up fighting the monster and it was even fight but your friend stepped in and you both overwhelmed the monster and defeated it. you find alot of food and bring it back to your friends. you and your friends are continue on escaping and fortunately you all made it without a problem. you and your friends escaped and reached happy ending")
            else:
                print("\n you chose wrong path and died.")
        else:
                print("\n you chose wrong path and died.")
    else:
                print("\n you chose wrong path and died.")


elif answer == "danger":
    answer = input("\n you and your friends went on a risky path but fortunately you and your friends dodge most of the attacks. one warrior ends up blocking your path. you can fight your way through or try to escape. type fight or escape: ")
    if answer == "escape":
        print("\n you try to run around but warrior ends up killing you and your friends.")
    elif answer == "fight":
        answer = input("\n you end up fighting and exchanged blows here and there but eventually you are the stronger one and overwhelmed the warrior and defeated him. you and your friends continue on fighting your way through but suddenly one of your friends got hit and fell down. you can escape or you can try saving your friend. type save or escape: " )
        if answer == "escape":
            print("\n you and your remaining friends end up leaving the friend and run for the escape. you all made it but one friend has been lost")
        elif answer == "save":
            answer = input("\n you end up going for brave move and saving your friend. you dodge the blows and saved your friend in time. the path to escape was blocked and you have no time to wait. you end up going for another path with your friends. then there is a a very strong warrior blocking your path and you have to fight through. will you fight or try to escape? type escape or fight: " )
            if answer == "escape":
                print("the warrior kills you and your friends")
            elif answer == "fight":
                answer = input("you and your friends are fighting the warrior but hes too strong. you have a strategy in mind and put it into action. you and your friends distract the warrior while one of your friends charge their strongest magic spell. you are all overwhelmed by him and he goes for your friend with magic spell. you can go for magic spell he casted and finish the warrior but its risky or you can attack the warrior to slow him down. type attack or magic " )
                if answer == "magic":
                    print("you tried to go for the magic spell but the warrior saw that and stopped you and killed you.")
                elif answer == "attack":
                    print("you attack the warrior and you try to slow him down with grabbing him. your other friend ends up with getting the magic spell just in time and attacks the warrior and defeats the warrior. you and your friends won a fierce battle and end up escaping. you all made it safe and sound and reached happy ending")
                else:
                   print("\n you chose wrong path and died.")
            else:
                   print("\n you chose wrong path and died.")
        else:
                   print("\n you chose wrong path and died.")
    else:
                   print("\n you chose wrong path and died.")



else:
    print("\n you chose wrong path and died.")
