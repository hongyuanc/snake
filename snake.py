#snake
from tkinter import *
import random

# game values
GAME_HEIGHT = 800
GAME_WIDTH = 800
SPEED = 50
SPACE_SIZE = 25
BODY_PARTS = 3
BACKGROUND = '#FFFFFF'
BODY_COLOR = '#6495ED'
FOOD_COLOR = '#B53737'

class Snake:
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
        

class Food:
    def __init__(self): 

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

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

        global score

        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if collision(snake) == True:
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    elif new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

def collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for BODY_PARTS in snake.coordinates[1:]:
        if x == snake.coordinates[0] and y == snake.coordinates[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Verdana',50), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 2*SPACE_SIZE,
                       font=('Verdana',30), text="Press r to try again", fill="black", tag="restart")

def restart_game():
    global snake, food, score, direction

    # Reset game variables to initial values
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    next_turn(snake, food)

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

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<r>', lambda event: restart_game())

snake = Snake()

food = Food()

next_turn(snake, food)

restart_button = Button(window, text="Restart", command=restart_game, font=('Verdana', 20))
restart_button.place(x=0, y=0)

window.mainloop()