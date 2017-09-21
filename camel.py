import random


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your")
print("desert trek and out run the natives.")


done = False
miles_traveled_for_user = 0
thirst = 0
camel_tiredness = 0
distance_traveled_by_natives = -20
drinks_in_canteen = 3


while not done:
    print("\n", end="")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    user_choice = input("Your choice? ")
    print("\n", end="")
    if user_choice.upper() == "Q":
        done = True
    elif user_choice.upper() == "E":
        print("Miles traveled: %d" % miles_traveled_for_user)
        print("Drinks in canteen: %d" % drinks_in_canteen)
        print("The natives are %d miles behind you." % (miles_traveled_for_user-distance_traveled_by_natives))
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("The camel is happy.")
        distance_traveled_by_natives = distance_traveled_by_natives + random.randrange(7,15)
    elif user_choice.upper() == "C":
        miles_traveled_full_speed = random.randrange(10,21)
        miles_traveled_for_user = miles_traveled_for_user + miles_traveled_full_speed
        print("You traveled %d miles." % miles_traveled_full_speed)
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1,4)
        distance_traveled_by_natives = distance_traveled_by_natives + random.randrange(7,15)
    elif user_choice.upper() == "B":
        miles_traveled_moderate_speed = random.randrange(5,13)
        miles_traveled_for_user = miles_traveled_for_user + miles_traveled_moderate_speed
        print("You traveled %d miles." % miles_traveled_moderate_speed)
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(0,2)
        distance_traveled_by_natives = distance_traveled_by_natives + random.randrange(7, 15)
    elif user_choice.upper() == "A":
        if drinks_in_canteen == 0:
            print("Oh, there is no water left in your canteen.")
        else:
            drinks_in_canteen = drinks_in_canteen - 1
            print("%d water left in canteen." % drinks_in_canteen)
            thirst = 0
    if (4 < thirst <= 6) and (not done):
        print("You are thirsty")
    elif thirst > 6 and (not done):
        print("You died of thirst")
        done = True
    if 5 < camel_tiredness <= 8 and (not done):
        print("Your camel is getting tired.")
    elif camel_tiredness > 8 and (not done):
        print("Your camel is dead.")
        done = True
    if ((miles_traveled_for_user - distance_traveled_by_natives) <= 0) and (not done):
        print("The natives have caught you!")
        done = True
    elif ((miles_traveled_for_user - distance_traveled_by_natives) < 15) and (not done):
        print("The natives are getting close!")
    if (miles_traveled_for_user >= 200) and (not done):
        print("You win!")
        done = True
    random_number = random.randrange(1,21)
    if random_number == 1 and (not done) and thirst <= 6 and camel_tiredness <= 8 and ((miles_traveled_for_user - distance_traveled_by_natives) > 0):
        print("Congratulations! You have found an oasis.")
        drinks_in_canteen = 3
        thirst = 0
        camel_tiredness = 0


print("This game is over.")

