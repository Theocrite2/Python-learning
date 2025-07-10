print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# if waterfall_choice.lower() == "enter": for case insensitive, .upper() works too
# waterfall_choice = input("...").lower().strip() in case user put space by accident
# \n to add space
# ctrl + / to hash a line (#) or after highlighting a few lines to make them #
# \ can be used as an "escape", for example \' will tell Python not to interpret ' as part of the code

waterfall_choice = input("\nYou've arrived to a thick waterfall, type 'enter' if you want to enter or 'continue' if you want to keep going into the jungle:\n").lower().strip()

if waterfall_choice == "enter":
    print("\nYou\'ve entered the waterfall and got eaten by a crocodile, game over!")
elif waterfall_choice == "continue":
    print("\nYou are continuing into the jungle.")
    river_choice = input("\nYou are facing a river, you don't have much time and have to decide, "
                         "should you cross it now or wait that river flow soften? Write 'now' or 'wait':\n").lower().strip()

    if river_choice == "now":
        print("Success! You got to the other side of the river and can continue your quest.")
        temple_door_choice = input("\nFinally you reach the temple where the treasure might be, "
                                   "there are 3 doors of different colours, red, blue or yellow. Type 'red' or 'blue' or 'yellow' and see what happens:\n")

        if temple_door_choice == "yellow":
            print("\nThe door opens, inside shines a treasure, you accomplished your quest!")
        elif temple_door_choice == "blue":
            print("\nThe temple is flooding, you have no way "
                  "to escape and eventually drown. \n\nGAME OVER!")
        elif temple_door_choice == "red":
            print("\nFire is getting everywhere around you, this is the end. \n\nGAME OVER!")

        else:
            print ("\nYou entered the wrong input.")


    elif river_choice == "wait":
        print("\nA tiger was watching you from the dark "
              "and now attacked you and ate you! Game over.")

    else:
        print("\nYou typed the wrong input.")

else:
    print("\nYou typed the wrong input.")



