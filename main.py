import tkinter as tk
from pygame import mixer

TILE_SIZE = (12, 16)# 12x16 px
SCALE = 4



class Game():
    pass

def main():
    root = tk.Tk()
    root.geometry("1152x960")
    root.resizable(False, False)
    root.title("Lost Souls")
    root.mainloop()

if __name__ == '__main__':
    main()
