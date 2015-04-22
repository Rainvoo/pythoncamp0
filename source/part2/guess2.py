# This is "Guess the number" 

import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

message = "Guess the number"
frame = simplegui.create_frame("Guess the number", 400, 180, 100)

def draw(canvas):
    canvas.draw_text(message, [30,105], 40, "Orange")

def range1():
    global g, t, r
    g = random.randrange(0, 100)
    t = 7
    r = 0
    print("\nchoose a number from 0-100.\nyou have " + str(t) + " times.\n")
    
def range2():
    global g, t, r 
    g = random.randrange(0, 1000)
    t = 10  
    r = 1
    print("\nchoose a number from 0-1000.\nyou have " + str(t) + " times.\n")

    
def new_game(guess):
    global g, t
    t = t-1
    if  r == 0  and (int(guess)<0 or int(guess)>100):
          print("please type a number from 0-100!\n")
    elif r == 1 and (int(guess)<0 or int(guess)>1000):
        print("please type a number from 0-1000!\n") 
    else:
        print("\nIs answer"+ str(guess) +"?\n")
        if int(guess) == g or t!= 0 :
            if int(guess) == g:
                print("bingo!\n ")   
                if r == 0:
                     range1()
                elif r == 1:
                     range2() 
            elif int(guess) < g:
                print("too low!\nyou have " + str(t) + " times.\n")
            elif int(guess) > g:
                print("too high!\nyou have " + str(t) + " times.\n")
        else:
            print("Sorry. You don't guess it!\nThe number is" + str(g) + ".\nWhy not try it again?\n")
            if r == 0:
                     frame.start()
                     range1()
            elif r == 1:
                     frame.start()
                     range2() 

# register event handlers for control elements
frame.add_input("\nplease type a number:\n", new_game, 40) 
frame.add_button("0-100", range1, 80)
frame.add_button("0-1000", range2, 80)
frame.set_draw_handler(draw)


# start frame
frame.start()
print("Game start!\nPlease choose a game.")