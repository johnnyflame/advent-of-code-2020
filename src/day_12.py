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


if __name__ == "__main__":
    input_data = get_data(day=12)
    ship = Ship()
    for action in input_data.splitlines():
        ship.perform_next_action(action)

    print(f"part A: {ship.manhatten_distance(0,0)}")
