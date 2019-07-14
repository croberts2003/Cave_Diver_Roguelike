import json
from colorama import init
init()
from colorama import Fore, Style
from entity import Player

class Render:
    tiles = []
    def generate(self):
        walls = [0, 1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 13, 20, 27, 34, 41, 48, 43, 44, 45, 46, 47]

        for _ in range(49):
            Style.RESET_ALL
            Render.tiles.append('-')
        self.append_player()
        for position in walls:
            Render.tiles[position] = Fore.LIGHTWHITE_EX + '~'

    def append_player(self):
        del Render.tiles[Player.pos]
        Render.tiles.insert((Player.pos), Player.char)

    def remove_player(self):
        player_pos = Render.tiles.index(Player.char)
        Render.tiles[player_pos] = '-'
        Style.RESET_ALL

    def output(self):
        for i in range(49):
            print(Render.tiles[i] + '  ', end = " ")
            if i == 6:
                print('\n')
            elif i == 13:
                print('\n')
            elif i == 20:
                print('\n')
            elif i == 27:
                print('\n')
            elif i == 34:
                print('\n')
            elif i == 41:
                print('\n')
            elif i == 48:
                print('\n')

