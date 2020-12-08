"""
Day 7 of Advent of code

Approach:

1. Parse input string into a graph representation
2. Do search on them

"""

from collections import deque
from typing import List, NamedTuple

from aocd import get_data


class Bag(NamedTuple):
    name: str
    children: dict

    def find_path_to_bag(self):
        pass

    @classmethod
    def from_string(cls, s):
        # TODO: how can the input be validated better?
        if not s:
            raise ValueError("Cannot create bag from empty string")
        words_in_input = s.split()
        bag_name = " ".join(words_in_input[:2])
        contains = {}

        # TODO: fix this hack
        for i, word in enumerate(words_in_input):
            if word.isnumeric():
                contains[" ".join(words_in_input[i + 1 : i + 3])] = int(word)

        print(f"bag {bag_name} contains {[x for x in contains]}")
        return Bag(bag_name, contains)


# TODO: can we make this less "bag specific"?
def bfs(start, goal_bag_name, bags):
    visited = set()
    queue = deque()

    queue.append(start)
    while queue:
        curr = bags[queue.popleft()]
        if not curr:
            raise ValueError(f"Unknown bag type : {curr}")
        for name in curr.children.keys():
            if name == goal_bag_name:
                return True
            if name not in visited:
                queue.append(name)
                visited.add(name)
    return False


def dfs(name, quantity, bags):
    curr = bags[name]
    if len(curr.children) == 0:
        return quantity

    total = quantity
    for child, num_children in curr.children.items():
        total += quantity * dfs(child, num_children, bags)

    return total


def create_bag_table(input):
    bags = {}
    for line in input.splitlines():
        new_bag = Bag.from_string(line)
        bags[new_bag.name] = new_bag

    assert len(bags) == len(input.splitlines())
    return bags


def count_bags_containing_target(bags, target_name=""):
    count = 0
    for bag in bags:
        if bfs(bag, target_name, bags=bags):
            count += 1
    return count


test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

test_input_first_line = (
    """light red bags contain 1 bright white bag, 2 muted yellow bags."""
)

test_input_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

test_bags_1 = create_bag_table(test_input)
assert count_bags_containing_target(test_bags_1, "shiny gold") == 4
# total minus the root bag
assert (dfs("shiny gold", 1, test_bags_1) - 1) == 32


test_bags_2 = create_bag_table(test_input_2)
assert (dfs("shiny gold", 1, test_bags_2) - 1) == 126


data = get_data(day=7)
bags = create_bag_table(data)
answer_first_part = count_bags_containing_target(bags, "shiny gold")
second_part = dfs("shiny gold", 1, bags) - 1

print(f"First answer: {answer_first_part}")
print(f"Second answer: {second_part}")
