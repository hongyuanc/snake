#snake

from tkinter import *
import random

# game values
GAME_HEIGHT = 800
GAME_WIDTH = 800
SPEED = 50
SPACE_SIZE = 100
BODY_PARTS = 3
BACKGROUND = '#FFFFFF'
BODY_COLOR = '#6495ED'
FOOD_COLOR = '#B53737'

class snake:
    pass

class food:
    def __init__(self): 
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

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
window.resizable(True, True)
                
score = 0
direction = 'down'

# displays score
label = Label(window, text='Score: {}'.format(score), font = ('Verdana', 40))
label.pack()

# displays the game board
canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# starts the console in the middle of the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = snake()

food = food()

window.mainloop()