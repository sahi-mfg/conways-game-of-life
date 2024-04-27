from flask import Flask, render_template, request, jsonify
from src.grid import Grid

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    initial_cells_alive = int(data["initial_cells_alive"])
    num_iterations = int(data["num_iterations"])

    grid = Grid((30, 30))
    grid.random_fill(initial_cells_alive)
    grid.set_neighbors()

    generations = []
    for _ in range(num_iterations):
        generation = [[cell.is_alive() for cell in row] for row in grid.grid]
        generations.append(generation)
        grid.game()
        grid.actualize_grid()

    return jsonify(generations)


if __name__ == "__main__":
    app.run(debug=True)
