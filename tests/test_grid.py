from src.grid import Grid


def test_is_in_grid():
    grid = Grid((10, 10))
    assert grid.is_in_grid(5, 5) is True
    assert grid.is_in_grid(-1, 5) is False
    assert grid.is_in_grid(5, 11) is False
    assert grid.is_in_grid(10, 10) is False


def test_is_neighbor():
    # Test for cells that are neighbors
    assert Grid.is_neighbor(0, 0, 0, 1) is True
    assert Grid.is_neighbor(0, 0, 1, 0) is True
    assert Grid.is_neighbor(0, 0, 1, 1) is True

    # Test for cells that are not neighbors
    assert Grid.is_neighbor(0, 0, 2, 0) is False
    assert Grid.is_neighbor(0, 0, 0, 2) is False
    assert Grid.is_neighbor(0, 0, 2, 2) is False
