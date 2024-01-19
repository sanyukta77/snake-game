import curses
import random
import time

# Initialize the screen
s = curses.initscr()

# Disable cursor display
curses.curs_set(0)

# Get the screen dimensions
sh, sw = s.getmaxyx()

# Create a new window
w = curses.newwin(sh, sw, 0, 0)

# Allow the window to capture key events
w.keypad(1)

# Set the refresh rate
w.timeout(100)

# Initialize the snake
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2],
]

# Initialize the food
food = [sh // 2, sw // 2]

# Display the initial food
w.addch(food[0], food[1], curses.ACS_PI)

# Set the initial movement direction
key = curses.KEY_RIGHT

# Start the game loop
while True:
    # Get the next key press
    next_key = w.getch()

    # If a key was pressed, update the movement direction
    if next_key != -1:
        key = next_key

    # Calculate the new head position based on the current direction
    head = snake[0]
    if key == curses.KEY_DOWN:
        new_head = [head[0] + 1, head[1]]
    elif key == curses.KEY_UP:
        new_head = [head[0] - 1, head[1]]
    elif key == curses.KEY_LEFT:
        new_head = [head[0], head[1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [head[0], head[1] + 1]

    # Insert the new head into the snake
    snake.insert(0, new_head)

    # Check if the snake has collided with the boundaries or itself
    if snake[0][0] in [0, sh - 1] or snake[0][1] in [0, sw - 1] or snake[0] in snake[1:]:

        curses.endwin()
        quit()

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')


    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    
    w.refresh()

  
    time.sleep(0.1)
