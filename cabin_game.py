import time


print("You are staying at a cabin in the depths of a dark and dangerous forest.")
response = input("You've come upon a river and a road that fork away from each other. Do you follow the road or the river? - Type yes for river and no for road -")
if response == "yes" or "Yes":
    print("As you follow the river, you notice a mysterious and hot lumberjack in the distance.")
    response = input("Should you approach him? - yes or no -")
    if response == "yes":
        print("As you catch his eye, you feel a sense of apprehension and he slowly saunters towards you. All of a sudden you feel like trapped prey and immediately regret your decision. ")
        response = input("Escape during day or night? - type day or night -")
        if response == "day":
            print("You escaped! But now you have a long journey ahead of you.")
            response = input("Do you want to cross the river? - yes or no -")
            if response == "Yes" or "yes":
                print("Cross river yes TBC")
            else:
                if response == "No" or "no":
                    print("You continue to wander through the forest for the next couple of days when you stumble upon a lonely camper. After your encounter with the lumberjack you are more cautious than ever of approaching strangers so you stake out in a nearby tree for the next few hours.")
                    print("In the distance, you hear joyful laughter, and a family comes into view. Your fear instantly dissipates and you consider asking for help.")
                    response = input("Ask the family for help? - yes or no -")
                    if response == "Yes" or "yes" or "YES":
                        print("Yay! The family helped you find your way back home. The end.")
                    else:
                        if response == "No" or "no" or "NO":
                            print

        else:
            if response == "night":
                print("The lumberjack's dog heard you sneak out the door and starts howling. You panic and run across the yard.")
                time.sleep(2.5)
                print("In your hurry, you trip over a tree stump and fall... You try to get up but you can't.")
                time.sleep(2.5)
                print("You see lights turn on in the house and you hear a door slam.")
                time.sleep(2.5)
                print("And in the dark haze, you see the lumberjack walking towards you and realize your escape failed.")
                time.sleep(3)
                print("You were caught. GAME OVER")
    else:
        if response == "No" or "no":
            print("You decide not to trust the man and avoided danger")
            time.sleep(1)
            print("As your walking you come across a dog that looks scarily similar to the dog you have at home.")
            time.sleep(2)
            response = input("The dog seems to know where it's going. Do you follow it? - yes or no -")
            if response == "yes" or "Yes":
                print("The dog recognizes you and leads you home where you find your family waiting. They are thrilled to see and have been waiting for hours. THE END!")
            if response == "No" or "no":
                print("Surpise!")
                time.sleep(1)
                print("The dog was actually a wolf who chases you deeper into the woods and you are lost forever. THE END!")


else:
    if response == "no":
        print("You follow the road for many miles and your energy is slowly draining. It has been two days since you ate or drank anything and your stomach is ravenous. As you continue walking, you see a suspicious lump in the distance and you decide to approach it. You soon discover that the lump is actually a deer killed by a car a few hours earlier.")
        response = input("Even though it does not look very appetizing, your stomach growls as you look it up and down. Do you eat it? - yes or no -")
        if response == "yes" or "Yes":
                print("You take out your pocket knife and slowly rip chunks of meat off of the animal and proceed to eat them. Your energy is restored but your stomach is turning and you feel extremely sick. Turns out the animal was not killed by a car, but it died of a contagious disease. DIE END")
        else:
            if response == "No" or "no":
                print("It turns out that you could hold off your hunger for a few more days. However, you find that your thirst is becoming increasingly unquenchable and prominently urgent. There is a notion of the water carrying disease in the back of your head, but your thirst outweighs your cautious reasoning.")
                response = input("Should you drink the water? -yes or no-")
                if response == "yes" or "Yes":
                    print("You collect some water with a large leaf that you find nearby. You notice that there are tools sufficient enough for you to start a fire to purify the water to kill the germs.")
                    response = input("Do you boil the water? - yes or no -")
                    if response == "Yes" or "yes":
                        print("You start a fire to purify the water and take a long, refreshing sip. Your eyelids began to feel very heavy and all you can think of is taking a nice long nap underneath the stars.")
                        time.sleep(.25)
                        response = input("Should you rest for a few hours or continue on your way? - rest or continue -")
                        if response == "Continue" or "continue":
                            print("You continue on your journey, and you soon find the cabin that your family is staying at, and you are reunited with your loved ones. You live happily ever after! THE END")


                    else:
                        if response == "No" or "no":
                            print("You die of thirst and never see your family ever again.")
                            time.sleep(.5)
                            print("If you had boiled the water you may have survived and felt the warmth of your bed once more...but alas you have come to THE END.")
