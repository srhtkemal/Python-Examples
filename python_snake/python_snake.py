import tkinter
import random
GAME_WIDTH = 700
GAME_HEIGHT = 700
GAME_SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([SPACE_SIZE, SPACE_SIZE])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="SNAKE")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        # GAME_WIDTH/SPACE_SIZE => 700/50 => 14
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y +
                           SPACE_SIZE, fill=FOOD_COLOR, tag="FOOD")


def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if (x==food.coordinates[0] and y==food.coordinates[1]):
        global game_score 
        game_score+=1
        label.config(text=f"Score: {game_score}")
        canvas.delete("FOOD")
        food=Food()
    else:
        del snake.coordinates[-1]  # Delete last body part
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if(check_collisions(snake)):
        game_over()
    else:
        window.after(GAME_SPEED, next_turn, snake, food)
        


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":  # Bc we don't want snake to move 180 degree
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):
    x,y=snake.coordinates[0]
    if(x<0 or x>=GAME_WIDTH or y<0 or y>=GAME_HEIGHT ):
        print("Game Over")
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(all)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,font=("consolas", 30), text=f"Game Over\nYour Score is: {game_score}", fill="red", tag="gameover" )

window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

game_score = 0
direction = "down"
label = tkinter.Label(
    window, text=f"Score: {game_score}", font=("consolas", 40))
label.pack()

canvas = tkinter.Canvas(window, bg=BACKGROUND_COLOR,
                        height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
# print(f"{window_width}x{window_height}+{x}+{y}")
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# lambda event is something like ()=>{} in JS
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
# print(window_height, window_width)

snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()
