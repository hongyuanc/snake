#snake

from tkinter import *
import random

# game values
GAME_HEIGHT = 800
GAME_WIDTH = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
BACKGROUND = '#FFFFFF'
BODY_COLOR = '#6495ED'
FOOD_COLOR = '#B53737'

class snake:
    def __init__(self):

        self.body_parts = BODY_PARTS
        self.body_color = BODY_COLOR
        self.speed = SPEED

        self.coordinates = []
        self.squares = []

        for x in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BODY_COLOR, tag="snake")
            self.squares.append(square)
        

class food:
    def __init__(self): 

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordiates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    else:
        x -= SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BODY_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

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