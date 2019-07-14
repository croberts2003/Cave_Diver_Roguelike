from entity import Player
from render import Render
from input_handler import check_inputs
from clear_terminal import clear

esc_key = False
new_map = Render()


while True:
    new_map.generate()
    new_map.output()
    check_inputs()





