from aocd import get_data
from requests.api import get


def two_sum(arr, target):
    inverse = set()
    for val in arr:
        if target - val in inverse:
            return True
        inverse.add(val)
    return False


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def part_1(arr, preamble=5):
    for i in range(preamble, len(arr)):
        sliding_window = arr[i - preamble : i]
        target = arr[i]
        if not two_sum(sliding_window, target):
            return target
    return None


def part_2(arr, target=0):
    for window_size in range(2, len(arr)):
        for i in range(window_size, len(arr) + 1):
            sliding_window = arr[i - window_size : i]
            if sum(sliding_window) == target:
                return min(sliding_window) + max(sliding_window)
    return None


test_data = [int(x) for x in test_input.splitlines()]
print(test_data)

assert part_1(test_data) == 127
assert part_2(test_data, 127) == 62
real_data = [int(x) for x in get_data(day=9).splitlines()]
target = part_1(real_data, preamble=25)
print(part_2(real_data, target))
