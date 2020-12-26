# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_number(name):
    "converts name to number"

    if (name == "rock"):
        name = 0
        return name
    elif (name == "Spock"):
        name = 1
        return name
    elif (name == "paper"):
        name = 2
        return name
    elif (name == "lizard"):
        name = 3
        return name
    elif (name == "scissors"):
        name = 4
        return name
    else:
        print "No cheating!"
        
        

def number_name(number):
    "converts number to name"
    
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else:
        print "???"

# Main function

import random

def rpsls(player_choice): 
    "takes player + computer choice"
    
    print " "
    print "You chose", player_choice
    player_number = name_number (player_choice)
    comp_number = random.randrange(0,4)
    comp_choice = number_name(comp_number)
    print "The computer chose", comp_choice
    difference = player_number - comp_number
        if difference 
    
    
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


