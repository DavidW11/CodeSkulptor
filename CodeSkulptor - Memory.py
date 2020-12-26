# Card Game - Memory

import simplegui
import random

turns = 0


def new_game():
    global cards
    global exposed
    global state
    global turns
    cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    random.shuffle(cards)
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    state = 0
    turns = 0
    label.set_text(str(turns))
    
def mouseclick(pos):
    global state
    global exposed
    global ind_1
    global ind_2
    global turns
    card_ind = int(pos[0]/50)
    if exposed[card_ind] == False:
        exposed[card_ind] = True
        turns += 1
        label.set_text(str(turns))
        if state == 0:
            state = 1
            ind_1 = card_ind
            #print "state is", state
            #print cards[ind_1]
        elif state == 1:
            state = 2
            ind_2 = card_ind
            #print "state is", state
            #print cards[ind_1]
            #print cards[ind_2]
        elif state == 2 and cards[ind_1] != cards[ind_2]:
            state = 1
            exposed [ind_1] = False
            exposed [ind_2] = False
            exposed [card_ind] = True
            ind_1 = card_ind
            ind_2 = 0
            #print "state is", state
            #print cards[ind_1]
            #print cards[ind_2]
        elif state == 2 and cards[ind_1] == cards[ind_2]:
            exposed [card_ind] = True
            state = 1
            ind_1 = card_ind
            ind_2 = 0
            #print "state is", state
            #print cards[ind_1]
            #print cards[ind_2]
    
def draw(canvas):
    global exposed
    for card_index in range(len(cards)):
        card_pos = 25 + 50 * card_index
        if exposed[card_index] == True:
            canvas.draw_text(str(cards[card_index]), (card_pos, 50), 21, "white")
        elif exposed[card_index] == False:
            canvas.draw_polygon([(card_pos-25, 0), (card_pos+25, 0), (card_pos+25, 100), (card_pos-25, 100)], 7, 'Black', 'Green')


frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("0")


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


new_game()
frame.start()