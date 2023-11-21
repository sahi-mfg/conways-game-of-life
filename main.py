from src.grid import Grid
import time


def delete_screen():
    print("\u001B[H\u001B[J")


def main():
    grid = Grid((50, 50))
    grid.random_fill(50)
    grid.set_neighbors()

    print("Conway's Game of Life")
    while True:
        delete_screen()
        print(grid)
        print("\n")
        time.sleep(0.8)
        grid.game()
        grid.actualize_grid()


if __name__ == "__main__":
    main()
