from collections import Counter
from fileinput import input

from aocd import get_data

test_input = """16
10
15
5
1
11
7
19
6
12
4
"""

test_input_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def sum_diff(input):
    data = [int(x) for x in input.splitlines()]
    outlet = 0
    device = max(data) + 3
    data.extend([outlet, device])
    data.sort()
    diff_counter = Counter()

    for prev, curr in zip(data, data[1:]):
        diff_counter[curr - prev] += 1

    return diff_counter[1] * diff_counter[3]


def find_all_arrangements(input):
    data = [int(x) for x in input.splitlines()]
    outlet = 0
    device = max(data) + 3
    data.extend([outlet, device])
    data.sort()
    dp_counter = Counter()
    dp_counter[0] = 1

    for val in data[1:]:
        dp_counter[val] = (
            dp_counter[val - 1] + dp_counter[val - 2] + dp_counter[val - 3]
        )

    return dp_counter[device]


assert sum_diff(test_input) == 35
assert sum_diff(test_input_2) == 220
assert find_all_arrangements(test_input) == 8
assert find_all_arrangements(test_input_2) == 19208

print(f"part A: {sum_diff(get_data(day=10))}")
print(f"part B: {find_all_arrangements(get_data(day=10))}")
