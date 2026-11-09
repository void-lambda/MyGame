import tkinter as tk
from pygame import mixer

from src.entity.entity import Entity
from world import World


WIN_WIDTH = 1152
WIN_HEIGHT = 960

# Main things
SCALE = 4

TILE_SIZE_W = 12  # 12 px
TILE_SIZE_H = 16  # 16 px

TILE_PIXELS_WIDTH = TILE_SIZE_W * SCALE
TILE_PIXELS_HEIGHT = TILE_SIZE_H * SCALE

class Game():
    def __init__(self, root):

        self.root = root

        # Window Parameters
        self.root.title("Lost Souls")
        self.root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.root.resizable(False, False)

        # World

        # Player

        # Camera

    def run(self):
        self.root.mainloop()

def main():
    # Initialize the Game
    root = tk.Tk()
    game = Game(root)
    game.run()

if __name__ == '__main__':
    main()
