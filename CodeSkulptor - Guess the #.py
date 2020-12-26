# Guess the number #


import random
import simplegui


# helper function to start and restart the game
secret_number = random.randrange(0,99)
number_guesses = 7
range = 100
def new_game():
    "starts new game with the right range and number of guesses"
    global range
    global secret_number
    global number_guesses
    if range == 100:
        range100()
        number_guesses = 7
    elif range == 1000:
        range1000()
        number_guesses = 10
    else:
        print "?"
        
    
    
# define event handlers for control panel
def range100():
    "changes range to 100"
    global range
    range = 100
    global secret_number
    secret_number = random.randrange(0,99)
    return secret_number

def range1000():
    "changes range to 1000"
    global range
    range = 1000
    global secret_number
    secret_number = random.randrange(0,999)
    return secret_number


#main logic
def input_guess(guess):
    "takes and prints guess, print higher or lower, print number of tries left"
    print "You guessed", guess
    if secret_number < int(guess):
        print "Lower"
        check_guesses()
    elif secret_number > int(guess):
        print "Higher"
        check_guesses()
    elif secret_number == int(guess):
        print "Correct!"
        new_game()
    else:
        print "???"
        
        
#checks number of guesses remaining        
def check_guesses():
    "checks number of guesses remaining"
    global number_guesses
    if number_guesses > 0:
        print "You have", number_guesses, "guesses remaining"
        print " "
        number_guesses -= 1
    elif number_guesses == 0:
        print "You have", number_guesses, "guesses remaining :( try again"
        print " "
        new_game()
    else:
        print "????"
        

# create frame
f = simplegui.create_frame("Guess the Number!",200,200)


# register event handlers for control elements and start frame
f.add_button("range(1,99)", range100, 200)
f.add_button("range(1,999)", range1000, 200)
f.add_input("Guess the Number!", input_guess, 300)