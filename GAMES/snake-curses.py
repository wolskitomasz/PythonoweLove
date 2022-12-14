import curses 
from random import randint

# ustawienia okna
curses.initscr()
win = curses.newwin(20, 60, 0, 0) # x, y
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# poczatkowe koordynaty weza i jedzenia
snake = [(4, 4), (4, 3), (4, 2)]
food = (6, 6)

win.addch(food[0], food[1], '#')


# logika gry
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # ustawienie szybkosci poruszania
    
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]: # brak klawisza = dalej ten sam kierunek
        key = prev_key
        
    # ustawianie nowych koordynatow
    y = snake[0][0]
    x = snake [0][1]
    
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
        
    snake.insert(0, (y, x))
    
    # uderzenie w sciane
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break
    
    # zjedzenie samego siebie
    if snake[0] in snake[1:]: break
    
    if snake[0] == food:
        # zjedzenie pozywienia
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # dodanie spacji za ogonem
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        
    win.addch(snake[0][0], snake[0][1], '*')
    
curses.endwin()
print(f'Final score = {score}')

# futures:
#     * przechodzenie na przeciwna strone ekranu zamiast konca gry po uderzeniu w ramke
#     * brak mozliwosci zrobienia 180 stopni obrotu zeby sie nie zjesc