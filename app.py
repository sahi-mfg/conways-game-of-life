from flask import Flask, render_template, request
from src.grid import Grid
import time

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    initial_cells_alive = int(data["initial_cells_alive"])
    num_iterations = int(data["num_iterations"])
    speed = float(data["speed"])

    grid = Grid((30, 30))
    grid.random_fill(initial_cells_alive)
    grid.set_neighbors()

    for _ in range(num_iterations):
        print(grid.grid)
        time.sleep(speed)
        grid.game()
        grid.actualize_grid()

    return grid.grid


if __name__ == "__main__":
    app.run(debug=True)
