import pytest
from src.day_12 import Ship, ShipUsingWayPoint


class Test_day_12:
    def test_simple_ship_movement(self):
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

    def test_waypoint(self):
        ship = ShipUsingWayPoint()
        ship.perform_next_action("F10")
        assert ship.coord == (100, 10)
        assert ship.waypoint == (110, 11)
        ship.perform_next_action("N3")
        assert ship.coord == (100, 10)
        assert ship.waypoint == (110, 14)
        ship.perform_next_action("F7")
        assert ship.coord == (170, 38)
        assert ship.waypoint == (180, 42)
        ship.perform_next_action("R90")
        assert ship.coord == (170, 38)
        assert ship.waypoint == (174, 28)
        ship.perform_next_action("F11")
        assert ship.coord == (214, -72)
        assert ship.waypoint == (218, -82)

    def test_rotation(self):
        ship = ShipUsingWayPoint(waypoint=(1, 4))
        ship.perform_next_action("R180")
        assert ship.waypoint == (-1, -4)
        ship.perform_next_action("R180")
        assert ship.waypoint == (1, 4)

        ship.perform_next_action("R90")
        assert ship.waypoint == (4, -1)
        ship.perform_next_action("R90")
        assert ship.waypoint == (-1, -4)
        ship.perform_next_action("R90")
        assert ship.waypoint == (-4, 1)
