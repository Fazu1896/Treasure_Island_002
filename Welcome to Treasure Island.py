print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("welcome to treasure island!")
print("Your mission is to find the treasure.")
print("You'r at a cross road. Where do you want to go?")
a = str(input('Type "left" or "right"\n'))
if a == "left" or a == "Left":
    print ("You come to a lake. There is a island in the middle of the lake.")
    
    b = str (input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')).lower()
    if b == "wait":
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        
        c = str(input("One red, one yellow and one blue. Which colour do you choose?\n")).lower()
        if c == "red":
            print ("You Found the treasure.You Win")
        elif c == "yellow":
            print ("pirates catch you! Game Over!")
        elif c == "blue":
            print ("Dead End! You decide to go back. Game Over!")
        else:
            print("Wrong input!!")
    else:
        print ("Game Over! Try again.")
else:
    print ("Game Over! You fell into a pit")
  
