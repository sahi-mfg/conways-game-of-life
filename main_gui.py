import tkinter as tk
from src.grid import Grid


class GameOfLifeGUI:
    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

    def draw_grid(self):
        for i, row in enumerate(self.grid.grid):
            for j, cell in enumerate(row):
                if cell.is_alive():
                    self.canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="black")
                else:
                    self.canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="white")

    def update(self):
        self.grid.game()
        self.draw_grid()
        self.root.after(100, self.update)  # Schedule next update

    def run(self):
        self.update()  # Start the game
        self.root.mainloop()  # Start the GUI event loop


# Usage:
grid = Grid((60, 60))
grid.random_fill(50)
gui = GameOfLifeGUI(grid)
gui.run()
