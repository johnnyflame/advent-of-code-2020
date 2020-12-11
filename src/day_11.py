from aocd import get_data

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def adjacent_neighbours(row, col, arr):
    X = len(arr)
    Y = len(arr[0])

    neighbors = lambda x, y: [
        (x2, y2)
        for x2 in range(x - 1, x + 2)
        for y2 in range(y - 1, y + 2)
        if (
            -1 < x < X
            and -1 < y < Y
            and (x != x2 or y != y2)
            and (0 <= x2 < X)
            and (0 <= y2 < Y)
        )
    ]
    return [arr[i][j] for (i, j) in neighbors(row, col)]


def find_first_neighbour_in_direction(
    row, col, row_increment, col_increment, arr, targets
):
    total_rows = len(arr)
    total_cols = len(arr[0])

    while (0 <= row < total_rows) and (0 <= col < total_cols):
        if arr[row][col] in targets:
            return arr[row][col]
        row += row_increment
        col += col_increment
    return None


def visible_neighbours(row, col, arr, targets=["#", "L"]):

    total_neighbours = [
        # going down
        find_first_neighbour_in_direction(row + 1, col, 1, 0, arr, targets)
        # going right
        ,
        find_first_neighbour_in_direction(row, col + 1, 0, 1, arr, targets)
        # going up
        ,
        find_first_neighbour_in_direction(row - 1, col, -1, 0, arr, targets)
        # going left
        ,
        find_first_neighbour_in_direction(row, col - 1, 0, -1, arr, targets)
        # down-left
        ,
        find_first_neighbour_in_direction(row + 1, col - 1, 1, -1, arr, targets)
        # down-right
        ,
        find_first_neighbour_in_direction(row + 1, col + 1, 1, 1, arr, targets)
        # up-right
        ,
        find_first_neighbour_in_direction(row - 1, col + 1, -1, 1, arr, targets)
        # up-left
        ,
        find_first_neighbour_in_direction(row - 1, col - 1, -1, -1, arr, targets),
    ]

    return total_neighbours


def mark_cells(input, neighbours, tolerance):
    remove = set()
    add = set()
    for row, line in enumerate(input):
        for col, val in enumerate(line):
            if val == ".":
                continue
            elif val == "#":
                if neighbours(row, col, input).count("#") >= tolerance:
                    remove.add((row, col))
            elif val == "L":
                if neighbours(row, col, input).count("#") == 0:
                    add.add((row, col))
    return add, remove


def change_cells(input, add, remove):
    output = [row[:] for row in input]
    for row, line in enumerate(input):
        for col, _ in enumerate(line):
            if (row, col) in add:
                output[row][col] = "#"
            elif (row, col) in remove:
                output[row][col] = "L"
    return output


def adjust_seating(data, neighbour_func, tolerance):
    old_count, new_count = float("inf"), float("-inf")

    while old_count != new_count:
        old_count = new_count
        add, remove = mark_cells(data, neighbour_func, tolerance=tolerance)
        data = change_cells(data, add, remove)
        new_count = sum(line.count("#") for line in data)
    return new_count


test_data = [list(x) for x in test_input.splitlines()]
assert adjust_seating(test_data, adjacent_neighbours, tolerance=4) == 37
assert adjust_seating(test_data, visible_neighbours, tolerance=5) == 26

data = [list(x) for x in get_data(day=11).splitlines()]
print(f"Part A: {adjust_seating(data, adjacent_neighbours, tolerance=4)}")
print(f"Part B answer: {adjust_seating(data, visible_neighbours, tolerance=5)}")
