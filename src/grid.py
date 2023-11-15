import random
from .cell import Cell


class Grid:
    def __init__(self, size: tuple = (10, 10)) -> None:
        self.size = size
        self.grid = [[Cell() for _ in range(size[1])] for _ in range(size[0])]

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def get_size(self):
        return self.size

    def get_cell(self, x: int, y: int):
        return self.grid[x][y]

    def set_cell(self, x: int, y: int, state: bool):
        self.grid[x][y].current_state = state

    def set_cell_neighbors(self, x: int, y: int):
        self.grid[x][y].set_neighbors(self.get_cell_neighbors(x, y))

    def get_cell_neighbors(self, x: int, y: int):
        neighbors = []
        for i in range(max(0, x - 1), min(self.size[0], x + 2)):
            for j in range(max(0, y - 1), min(self.size[1], y + 2)):
                if (i, j) != (x, y):
                    neighbors.append(self.get_cell(i, j))
        return neighbors

    @staticmethod
    def is_neighbor(self, x: int, y: int, x2: int, y2: int):
        return (x2, y2) in [
            (i, j)
            for i in range(max(0, x - 1), min(self.size[0], x + 2))
            for j in range(max(0, y - 1), min(self.size[1], y + 2))
            if (i, j) != (x, y)
        ]

    def is_in_grid(self, x: int, y: int):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def random_fill(self, cell_count: int = 0):
        flat_grid = [cell for row in self.grid for cell in row]
        for cell in random.sample(flat_grid, cell_count):
            cell.current_state = True

    def game(self):
        new_grid = [[Cell() for _ in range(self.size[1])] for _ in range(self.size[0])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                neighbors_count = self.get_cell_neighbors_count(i, j)
                new_grid[i][j].current_state = self.grid[i][j].compute_future_state(neighbors_count)
        self.grid = new_grid

    def actualize_grid(self):
        self.game()
