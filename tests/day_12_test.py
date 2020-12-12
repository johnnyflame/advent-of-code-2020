import pytest
from src.day_12 import Ship


class Test_day_12:
    def test_ship_move_simple_directions(self):
        input_data = """F10
N3
F7
R90
F11
"""
        ship = Ship()
        for action in input_data.splitlines():
            ship.perform_next_action(action)
        assert ship.coord == (17, -8)
        assert ship.manhatten_distance(0, 0)
