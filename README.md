# Python implementation of Conway's game of life.

The Game of Life was invented by British mathematician John H. Conway (1937-2020). It's an example of what's known as a two-dimensional cellular automaton. It runs on a rectangular array $(L \times H)$ of cells. A cell is represented by its coordinates $x$ and $y$, which verify $0 \leqsant x < L$ and $0 \leqsant y < H$.
A cell can be in two states: alive or dead. The dynamics of the game are expressed by the following transition rules:

a living cell remains alive in the next generation if it is surrounded by 2 or 3 living neighbors; otherwise, it dies;
a dead cell becomes alive in the next generation if it has exactly 3 living neighbors.

The notion of "neighborhood" in the Game of Life is that of the 8 cells that can surround a given cell (known as Moore's neighborhood).

The game is played on an infinite grid, but in practice, we limit ourselves to a finite grid, which is initialized with a certain number of living cells. The game is then iterated by applying the transition rules to each cell of the grid. The game is said to be in a stable state if no cell changes state from one generation to the next, or if the grid is empty. The game is said to be in an oscillating state if it returns to a previous state after a certain number of generations. The game is said to be in a chaotic state if it does not return to a previous state after a certain number of generations.


We used python and object oriented programming to implement the game it and we created an interface with streamlit to display it.

# How to run it

- Clone the repository: `git clone https://github.com/momosahi/conways-game-of-life.git` or `git clone git@github.com:momosahi/conways-game-of-life.git`
- Go to the directory: `cd conways-game-of-life`
- install the requirements: `pip install -r requirements.txt`
- Run the game: `python -m streamlit run main.py`


