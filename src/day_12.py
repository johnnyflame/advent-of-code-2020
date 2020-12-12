from aocd.get import get_data


class Ship:
    def __init__(self):
        # how can we represent this as an angle?
        self.rotation = 0
        self.coord = (0, 0)

    def get_direction(self):
        if self.rotation == 0:
            return "E"
        elif self.rotation == 90:
            return "S"
        elif self.rotation == 180:
            return "W"
        elif self.rotation == 270:
            return "N"
        else:
            raise ValueError(
                f"Only support 4 directions currently. degree {self.rotation} is not supported"
            )

    def move(self, direction, magnitude):
        curr_x, curr_y = self.coord
        if direction == "N":
            self.coord = (curr_x, curr_y + magnitude)
        elif direction == "S":
            self.coord = (curr_x, curr_y - magnitude)
        elif direction == "E":
            self.coord = (curr_x + magnitude, curr_y)
        elif direction == "W":
            self.coord = (curr_x - magnitude, curr_y)
        else:
            raise ValueError(
                f"Aceept directions in N,S,E,W and F, received {direction}"
            )

    def rotate(self, value):
        self.rotation = (self.rotation + value) % 360

    def perform_next_action(self, s):
        action = s[0]
        value = int(s[1:])

        if action == "R":
            self.rotate(value)
        elif action == "L":
            self.rotate(-value)
        elif action == "F":
            self.move(self.get_direction(), value)
        else:
            self.move(action, value)

    def manhatten_distance(self, dest_x, dest_y):
        curr_x, curr_y = self.coord
        return abs(curr_x - dest_x) + abs(curr_y - dest_y)


class ShipUsingWayPoint:
    def __init__(self, waypoint=(10, 1)):
        self.coord = (0, 0)
        self.waypoint = waypoint

    def rotate_waypoint(self, degrees):

        degrees = degrees % 360
        wp_x, wp_y = self.waypoint
        diff_x = self.coord[0] - wp_x
        diff_y = self.coord[1] - wp_y
        if degrees == 90:
            self.waypoint = (self.coord[0] - diff_y, self.coord[1] + diff_x)
        elif degrees == 180:
            self.waypoint = (self.coord[0] + diff_x, self.coord[1] + diff_y)
        elif degrees == 270:
            self.waypoint = (self.coord[0] + diff_y, self.coord[1] - diff_x)

    def move_ship_to_way_point(self, unit):
        # move the ship
        curr_x, curr_y = self.coord
        wp_x, wp_y = self.waypoint
        diff_x = wp_x - curr_x
        diff_y = wp_y - curr_y
        self.coord = (
            curr_x + (diff_x * unit),
            curr_y + (diff_y * unit),
        )
        # update the way point
        self.waypoint = (self.coord[0] + diff_x, self.coord[1] + diff_y)

    def move_waypoint(self, direction, magnitude):
        curr_x, curr_y = self.waypoint
        if direction == "N":
            self.waypoint = (curr_x, curr_y + magnitude)
        elif direction == "S":
            self.waypoint = (curr_x, curr_y - magnitude)
        elif direction == "E":
            self.waypoint = (curr_x + magnitude, curr_y)
        elif direction == "W":
            self.waypoint = (curr_x - magnitude, curr_y)
        elif direction == "R":
            self.rotate_waypoint(magnitude)
        elif direction == "L":
            self.rotate_waypoint(-magnitude)
        else:
            raise ValueError(
                f"Aceept directions in N,S,E,W and F, received {direction}"
            )

    def perform_next_action(self, s):
        action = s[0]
        value = int(s[1:])

        if action == "F":
            self.move_ship_to_way_point(value)
        else:
            self.move_waypoint(action, value)

    def manhatten_distance(self, dest_x, dest_y):
        curr_x, curr_y = self.coord
        return abs(curr_x - dest_x) + abs(curr_y - dest_y)


if __name__ == "__main__":
    actions = get_data(day=12).splitlines()
    ship = Ship()
    for action in actions:
        ship.perform_next_action(action)

    print(f"part A: {ship.manhatten_distance(0,0)}")

    ship = ShipUsingWayPoint()
    for action in actions:
        ship.perform_next_action(action)
    print(f"part B: {ship.manhatten_distance(0,0)}")
