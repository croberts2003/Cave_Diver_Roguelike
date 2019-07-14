from sys import exit

from render import Render
from entity import Player

def check_inputs():
    invalid_positions = [0, 1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 13, 20, 27, 34, 41, 48, 43, 44, 45, 46, 47]

    key = input()

    if key == 'w':
        Player.pos -= 7
    elif key == 's':
        Player.pos += 7
    elif key == 'a':
        Player.pos -= 1
    elif key == 'd':
        Player.pos += 1

    for position in invalid_positions:
        if position == Player.pos:
            if key == 'w':
                Player.pos += 7
            elif key == 's':
                Player.pos -= 7
            elif key == 'a':
                Player.pos += 1
            elif key == 'd':
                Player.pos -= 1
            print('You hit a wall!')
        
    if key == 'q':
        exit()

    remove = Render()
    remove.remove_player()
