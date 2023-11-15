from src.grid import Grid
import time


def main():
    grid = Grid((10, 10))
    grid.random_fill(50)
    while True:
        print(grid)
        print("\n")
        time.sleep(0.5)
        grid.game()
        grid.actualize_grid()


if __name__ == "__main__":
    main()
