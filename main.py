from src.grid import Grid
import time


def delete_screen():
    print("\033[H\033[J", end="")


def main():
    grid = Grid((20, 30))
    grid.random_fill(50)
    grid.set_neighbors()
    while True:
        delete_screen()
        print(grid)
        print("\n")
        time.sleep(0.5)
        grid.game()
        grid.actualize_grid()


if __name__ == "__main__":
    main()
