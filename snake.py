import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint


## default settings
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT
score = 0

snake = [[4,10], [4,9], [4,8]]
food = [10,20]

win.addch(food[0], food[1], '*')

## end of settings

##game 

while key != 27:
    win.border(0)
    win.addstr(0, 2, 'Score: ' + str(score) + ' ')
    win.addstr(0, 27, ' SNAKE ')
    win.timeout(120 - int((len(snake)/5 + len(snake)/10)%120)) ### speeeeeed

    prevKey = key
    event = win.getch()
    key = key if event == -1 else event 

    if key == ord(' '): ##if pressed key is space wait for antoher to resume game :D
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in (KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, 27):
        key = prevKey

    ### calculates new coords of snake's head

    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    ### reaching the borders

    if snake[0][0] == 0: break #snake[0][0] = 18
    if snake[0][1] == 0: break #snake[0][0] = 58
    if snake[0][0] == 19: break #snake[0][0] = 1
    if snake[0][1] == 59: break #snake[0][1] = 1

    ### if snake runs over itself XD 

    if snake[0] in snake[1:]: break

    ### eating foooooooooooood

    if snake[0] == food:
        food = []
        score+=1
        while food == []:
            food = [randint(1,18), randint(1,58)] ### new cords of food
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print("\nScore - " + str(score))




