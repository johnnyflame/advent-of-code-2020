from aocd import get_data


def check_slopes(data, step_x, step_y):
    curr_col = 0
    curr_row = 0
    count = 0
    data = data.splitlines()

    while curr_row < len(data):
        if data[curr_row][curr_col] == "#":
            count += 1

        row = data[curr_row]
        curr_col = (curr_col + step_x) % len(row)
        curr_row += step_y
    return count


input_data = get_data(day=3)

print(
    check_slopes(input_data, 3, 1)
    * check_slopes(input_data, 1, 1)
    * check_slopes(input_data, 5, 1)
    * check_slopes(input_data, 7, 1)
    * check_slopes(input_data, 1, 2)
)
