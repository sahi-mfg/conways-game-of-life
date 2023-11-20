import random
from .cell import Cell


class Grid:
    """The grid of the game. It is a 2D array of cells."""

    def __init__(self, size: tuple = (10, 10)) -> None:
        """initialize the grid.

        Parameters
        ----------
        size : tuple, optional
            size of the grid, by default (10, 10)
        """
        self.size = size
        self.grid = self.set_grid()

    def set_grid(self):
        """build the grid.

        Returns
        -------
        2D array (list of lists)
            the grid.
        """
        grid = [[Cell() for j in range(self.size[1])] for i in range(self.size[0])]
        return grid

    def get_cell(self, x: int, y: int) -> Cell:
        """get the cell at the given position.

        Parameters
        ----------
        x : int
            the x coordinate of the cell.
        y : int
            the y coordinate of the cell.

        Returns
        -------
        Cell
            the cell at the given position.

        Raises
        ------
        IndexError
            if the cell is not in the grid.
        """
        if self.is_in_grid(x, y):
            return self.grid[x][y]
        else:
            raise IndexError(f"Cell ({x}, {y}) not in grid")

    def set_cell(self, x: int, y: int, cell: Cell):
        """set the cell at the given position.

        Parameters
        ----------
        x : int
            the x coordinate of the cell.
        y : int
            the y coordinate of the cell.
        cell : Cell
            the cell to set.

        Raises
        ------
        IndexError
            if the x or y coordinate is not in the grid.
        """
        if self.is_in_grid(x, y):
            self.grid[x][y] = cell
        else:
            raise IndexError(f"Cell ({x}, {y}) not in grid")

    def __str__(self):
        """the grid representation."""
        string = ""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                string += str(self.get_cell(i, j)) + " "
            string += "\n"
        return string

    def set_neighbors(self) -> None:
        """set the neighbors of each cell."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                cell = self.get_cell(i, j)
                cell.set_neighbors(self.get_neighbors(i, j))

    def get_neighbors(self, x: int, y: int) -> list:
        """get the neighbors of the cell at the given position.

        Parameters
        ----------
        x : int
            the x coordinate of the cell.
        y : int
            the y coordinate of the cell.

        Returns
        -------
        list
            the cell's neighbors.
        """
        neighbors = []
        for i in range(max(0, x - 1), min(self.size[0], x + 2)):
            for j in range(max(0, y - 1), min(self.size[1], y + 2)):
                if self.is_in_grid(i, j) and self.is_neighbor(x, y, i, j):
                    neighbors.append(self.get_cell(i, j))
        return neighbors

    @staticmethod
    def is_neighbor(x: int, y: int, x2: int, y2: int) -> bool:
        """check if a cell at a given position is a neighbor of another cell at a given position.

        Parameters
        ----------
        x : int
            the x coordinate of the first cell.
        y : int
            the y coordinate of the first cell.
        x2 : int
            the x coordinate of the second cell.
        y2 : int
            the y coordinate of the second cell.

        Returns
        -------
        bool
            whether the second cell is a neighbor of the first cell.
        """
        return abs(x - x2) == 1 or abs(y - y2) == 1

    def is_in_grid(self, x: int, y: int) -> bool:
        """check if a cell at a given position is in the grid.

        Parameters
        ----------
        x : int
            the x coordinate of the cell.
        y : int
            the y coordinate of the cell.

        Returns
        -------
        bool
            whether the cell is in the grid.
        """
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def random_fill(self, cell_count: int = 0) -> None:
        """randomly fill the grid."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if random.random() <= (cell_count / 100):
                    cell = self.get_cell(i, j)
                    cell.live()
                    cell.switch_state()

    def game(self) -> None:
        """compute the future state of each cell."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                cell = self.get_cell(i, j)
                cell.compute_future_state()

    def actualize_grid(self) -> None:
        """switch the cells in their future state."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                cell = self.get_cell(i, j)
                cell.switch_state()
