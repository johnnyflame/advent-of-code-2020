from aocd import get_data


def binary_search(low, high, instructions):
    curr = 0
    up = {"B", "R"}
    down = {"F", "L"}
    while high > low and curr < len(instructions):
        curr_instruction = instructions[curr]
        mid = (high + low) // 2
        if curr_instruction in down:
            high = mid
        elif curr_instruction in up:
            low = mid + 1
        else:
            raise ValueError
        curr += 1
    return high


def find_seat(input):
    assert len(input) == 10
    row = binary_search(0, NUM_ROWS, input[:7])
    col = binary_search(0, NUM_COLS, input[7:])
    seat_id = 8 * row + col
    return row, col, seat_id


data = get_data(day=5)
tickets = data.splitlines()
NUM_ROWS = 127
NUM_COLS = 7

# test cases
assert binary_search(0, NUM_ROWS, "FBFBBFF") == 44
assert binary_search(0, NUM_COLS, "RLR") == 5
assert binary_search(0, NUM_ROWS, "BFFFBBF") == 70
assert find_seat("BFFFBBFRRR") == (70, 7, 567)
assert find_seat("FFFBBBFRRR") == (14, 7, 119)
assert find_seat("BBFFBBFRLL") == (102, 4, 820)


seat_ids = [find_seat(ticket)[2] for ticket in tickets]

max_id = max(seat_ids)
min_id = min(seat_ids)

all_vals = {val for val in range(min_id, max_id)}

print(f"part A answer: {max_id}")
print(f"part B answer: {all_vals.difference(seat_ids)}")
