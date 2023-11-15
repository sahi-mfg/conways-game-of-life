from src.grid import Grid
import time
import streamlit as st


def format_grid(grid):
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid.grid)


def main():
    grid_size = st.slider("Grid size", min_value=10, max_value=100, value=20)
    initial_live_cells = st.slider("Initial live cells", min_value=0, max_value=100, value=50)
    grid = Grid((grid_size, grid_size))
    grid.random_fill(initial_live_cells)
    grid.set_neighbors()

    speed = st.sidebar.slider("Speed", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
    if st.sidebar.button("Clear"):
        grid = Grid((grid_size, grid_size))

    if st.sidebar.button("Random"):
        grid.random_fill(initial_live_cells)
        grid.set_neighbors()

    if st.sidebar.button("Step"):
        st.text(format_grid(grid))
        time.sleep(speed)
        grid.game()
        grid.actualize_grid()


if __name__ == "__main__":
    st.title("Conway's Game of Life")
    main()
