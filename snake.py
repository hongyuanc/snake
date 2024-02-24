#snake

from tkinter import *
import random

# game values
GAME_HEIGHT = 1000
GAME_WIDTH = 1000
SPEED = 50
SPACE_SIZE = 100
BODY_PARTS = 3
class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(direction):
    pass

def collision():
    pass

def game_over():
    pass

def restart_game():
    pass

# interactive console
window = Tk()
window.title('Snake')
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text='Score:{}'.format(score))

window.mainloop()