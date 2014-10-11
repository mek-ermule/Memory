# Mekedelawit E. Hailu 

# Memory - Card Game

import simplegui
import random

cards_list = []
exposed = 0
card_opened = []
counter = 0
turns = 0

# helper function to initialize globals
def new_game():
    global cards_list, exposed, card_opened, counter, turns
    
    cards_list = [i for i in range(8)] + [i for i in range(8)]
    random.shuffle(cards_list)
    exposed = [False for i in range(16)]
    card_opened = []
    counter = 0
    turns = 0    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global counter, turns
    
    if counter == 0:
        card_opened.append(pos[0] / 50)
        exposed[pos[0] / 50] = True
        counter += 1
        turns = 1
        
    elif counter == 1:
        if not (pos[0] / 50 in card_opened):
            card_opened.append(pos[0] / 50)
            counter += 1
        exposed[pos[0] / 50] = True
       
    else:
        if not (pos[0] / 50 in card_opened):
            if cards_list[card_opened[-1]] != cards_list[card_opened[-2]]:
                exposed[card_opened[-1]] = False
                exposed[card_opened[-2]] = False
                card_opened.pop()
                card_opened.pop()
            counter = 1
            turns += 1
            exposed[pos[0] / 50] = True
            card_opened.append(pos[0] / 50)    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turns))
    for i in range(16):
        canvas.draw_line([50 * (i % 15 + 1), 0], [50 * (i % 15 + 1), 100], 2, "Green")
        if exposed[i]:
            canvas.draw_text(str(cards_list[i]), [15 + 50 * i, 70], 50, "Green")
         
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# call new_game and start frame
new_game()
frame.start()
