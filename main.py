from src.grid import Grid
import time


def delete_screen():
    print("\u001B[H\u001B[J")


def main():
    print("Conway's Game of Life")
    intial_cells_alive = int(input("Choose the number of intial cells alive: "))
    num_iterations = int(input("After how many generations should the game stop ?: "))
    speed = float(input("Ajust the speed of the game. The number should be between 0.1 (faster) and 1 (slower): "))

    grid = Grid((30, 30))
    grid.random_fill(intial_cells_alive)
    grid.set_neighbors()

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
