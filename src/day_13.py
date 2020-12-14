from datetime import time
from sys import maxsize

from aocd import get_data

test_data = """939
7,13,x,x,59,x,31,19
"""


def preprocess(raw_input):
    """
    parse input string and returns the start time and a list of buses.
    """
    start_time, buses = raw_input.splitlines()
    return int(start_time), [int(bus) for bus in buses.split(",") if bus != "x"]


def find_first_bus(raw_input):
    start_time, buses = preprocess(raw_input)
    for timestamp in range(start_time, start_time + max(buses)):
        for bus in buses:
            if timestamp % bus == 0:
                return timestamp - start_time, bus


def find_consecutive_busses(raw_input):
    # let's solve it incorrectly first, without considering the x in between
    _, buses = raw_input.splitlines()
    buses = buses.split(",")
    buses = [(i, int(bus)) for i, bus in enumerate(buses) if bus.isnumeric()]

    timestamp = 0
    inc = 1
    for offset, bus in buses:
        while (timestamp + offset) % bus != 0:
            timestamp += inc
        inc *= bus
    return timestamp


def find_largest_val_and_idx(items):
    largest_val = float("-inf")
    largest_idx = -1
    for i, item in enumerate(items):
        if item.isnumeric() and int(item) > largest_val:
            largest_val = int(item)
            largest_idx = i
    return largest_val, largest_idx


def check_list_divisibility(start, arr):
    for i, val in enumerate(arr, start):
        if val.isalpha():
            continue
        if i % int(val) != 0:
            return False
    return True


data = get_data(day=13)
wait_time, first_bus = find_first_bus(data)
print(f"Part A: {wait_time * first_bus}")

test_input = """939
67,x,7,59,61"""
assert find_consecutive_busses(test_input) == 779210

test_input = """939
67,7,x,59,61"""
assert find_consecutive_busses(test_input) == 1261476

test_input = """939
1789,37,47,1889"""
assert find_consecutive_busses(test_input) == 1202161486


print(f"Part B: {find_consecutive_busses(data)}")
