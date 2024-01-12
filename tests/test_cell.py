from src.cell import Cell


def test_is_alive():
    cell = Cell(current_state=True)
    assert cell.is_alive() is True

    cell = Cell(current_state=False)
    assert not cell.is_alive()


def test_set_alive():
    cell = Cell(current_state=False)
    cell.set_alive()
    assert cell.is_alive() is True


def test_set_dead():
    cell = Cell(current_state=True)
    cell.set_dead()
    assert not cell.is_alive()


def test_set_future_state():
    cell = Cell(future_state=False)
    cell.set_future_state(True)
    assert cell.future_state is True

    cell.set_future_state(False)
    assert not cell.future_state
