from random import randint
'''
Name: Seth Stoudenmier

Purpose: A text version of the board game "Haba's My First Orchard"

Statement of Authenticity: This program was done by myself with no outside help.
'''
# initializing a list that will represent the four fruits
fruit_list = [4,4,4,4]    # red, green, purple, yellow
#fruit_list = [2,2,2,2]     # fruit_list used for testing

# initializing the steps that the raven has
raven_steps = 4
#raven_steps = 2     # raven_steps used for testing

# initializing a list that will represent the die used for the game /
# also 2he variable that will hold the current die roll
die = ["0","1","2","3","basket","raven"]
roll = ""

# initializing a control variable for when to end the game
play = True

# initializing a variable to tell whose turn it is
player_turn = 0

# intializing the temp variable that holds the choice made when basket is rolled
basket_temp = 0

# prompting for the number of players and their names
player_list = []

# handles if the user does not give any input
while True:
    try:
        num_players = eval(input("How many people will be playing the game (1-4): "))
        break
    except (SyntaxError,NameError):
        print("Not valid input. Please give valid input.")
        
# handles input not within the required range
while (num_players<1 or num_players>4):
    while True:
        try:
            print("Not valid input. Please give valid input.")
            num_players = eval(input("How many people will be playing the game (1-4): "))
            break
        except (SyntaxError,NameError):
            print("",end="")
# builds the list of player names
for i in range(num_players):
    player_list.append(input("What is the name of player " + str(i+1) + ": "))

# a while loop that will play the game
while (play):
    # used to reset the player_turn variable back to the first player after
    # everyone has had a turn
    if (player_turn == len(player_list)):
        player_turn = 0
    # allows the player to specify when they want to die so it adds more control
    input((player_list[player_turn]) + " press return key when you are ready to roll the die.")
    # generates a randon int that indexes into the die[] to find what the roll is
    roll = die[randint(0,5)]
    #roll = die[eval(input("Input a die roll: "))]     # used to input a die roll for testing
    # logic to handle the die roll
    if (roll == "raven"):
        print("",end="   ")
        print(player_list[player_turn],"rolls a raven so the raven takes a step.")
        raven_steps-=1
    elif (roll == "basket"):
        # prompts the user for input on which fruit you want to remove
        print("  ",player_list[player_turn],"rolled a basket!!!")
        # print the remaining fruits so that a choice can be made
        if (fruit_list[0] > 0):
            print("   1: Red Apple")
        if (fruit_list[1] > 0):
            print("   2: Green Apple")
        if (fruit_list[2] > 0):
            print("   3: Purple Plum")
        if (fruit_list[3] > 0):
            print("   4: Yellow Pear")
        # gets the user's input on which fruit to remove
        while True:
            try:
                basket_temp = eval(input("   Enter the corresponding number to remove the color you want: "))
                break
            except (SyntaxError,NameError):
                print("   Not a valid number.")
        # handles bad input from the user based on the fruit that are remaining
        while (basket_temp<1 or basket_temp>4 or fruit_list[basket_temp-1]==0):
            print("   Not a valid number.")
            while True:
                try:
                    basket_temp = eval(input("   Enter the corresponding number to "+
                                             "remove the color you want: "))
                    if (1<=basket_temp<=4 and not fruit_list[basket_temp-1]==0):
                        if (fruit_list[basket_temp-1] == 0):
                                basket_temp = -1
                    break
                except (SyntaxError,NameError):
                    print("   Not a valid number.")
        fruit_list[basket_temp -1]-=1
    elif (0 <= eval(roll) <= 3):
        if (fruit_list[eval(roll)] != 0):
            fruit_list[eval(roll)]-=1
            print("",end="   ")
            if (eval(roll) == 0):
                print(player_list[player_turn],"rolls red so",player_list[player_turn],
                      "picks a red apple.")
            elif (eval(roll) == 1):
                print(player_list[player_turn],"rolls green so",player_list[player_turn],
                      "picks a green apple.")
            elif (eval(roll) == 2):
                print(player_list[player_turn],"rolls purple so",player_list[player_turn],
                      "picks a purple plum.")
            elif (eval(roll) == 3):
                print(player_list[player_turn],"rolls yellow so",player_list[player_turn],
                      "picks a yellow pear.")
        else:
            print("",end="   ")
            if (eval(roll) == 0):
                print(player_list[player_turn],"rolls red, but there are no more.")
            elif (eval(roll) == 1):
                print(player_list[player_turn],"rolls green, but there are no more.")
            elif (eval(roll) == 2):
                print(player_list[player_turn],"rolls purple, but there are no more.")
            elif (eval(roll) == 3):
                print(player_list[player_turn],"rolls yellow, but there are no more.")            
        
    # prints the current state of the game
    print("   Current Status:----------------------------------------------")
    print("   Red Apples:",fruit_list[0])
    print("   Green Apples:",fruit_list[1])
    print("   Purple Plum:",fruit_list[2])
    print("   Yellow Pear:",fruit_list[3])
    print("   Raven's Steps Needed:",raven_steps)
    print("   -------------------------------------------------------------")
    # checks to see if the game is over or not
    if (sum(fruit_list) == 0 or raven_steps == 0):
        play = False
    player_turn+=1

# informs the players if they won or lost the game
if (sum(fruit_list) == 0):
    print("You won the game!")
else:
    print("You lost the game. Better luck next time!")
