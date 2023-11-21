from src.grid import Grid
import time


def delete_screen():
    print("\u001B[H\u001B[J")


def main():
    grid = Grid((30, 30))
    grid.random_fill(50)
    grid.set_neighbors()

    print("Conway's Game of Life")
    num_iterations = int(input("After how many iteration should the game stop ?: "))
    print("\n")
    speed = float(input("Ajust the speed of the game. The number should be between 0.1 (faster) and 1 (slower): "))

    for _ in range(num_iterations):
        delete_screen()
        print(grid)
        print("\n")
        time.sleep(speed)
        grid.game()
        grid.actualize_grid()

    print("Game stopped.")


if __name__ == "__main__":
    main()
