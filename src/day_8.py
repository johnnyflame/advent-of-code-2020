from os import access
from os.path import split

from aocd import get_data
from requests.api import options

test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def detect_cycle(instructions):
    idx = 0
    accum = 0
    visited = set()
    has_cycle = False
    while idx < len(instructions):
        if idx in visited or idx < 0:
            has_cycle = True
            break
        instruction, arg = instructions[idx].split()
        visited.add(idx)
        if instruction == "nop":
            idx += 1
        elif instruction == "acc":
            accum += int(arg)
            idx += 1
        elif instruction == "jmp":
            idx += int(arg)
        else:
            raise ValueError(
                f"valid instructions are nop, acc and jmp, received {instruction}"
            )
    return has_cycle, accum


# O(n^2) brute force solution
def fix_instructions_brute_force(instructions):
    cycle, accum = detect_cycle(instructions)
    if cycle:
        options = {"jmp", "nop"}
        for i, line in enumerate(instructions):
            accum = 0
            instruction, arg = line.split()
            if instruction in options:
                new_instructions = [val for val in instructions]
                new_instructions[i] = list(options - {instruction})[0] + " " + arg
                cycle, accum = detect_cycle(new_instructions)
                if not cycle:
                    break
    return accum


test_data = [line for line in test_input.splitlines()]
assert detect_cycle(test_data) == (True, 5)
print(fix_instructions_brute_force(test_data))
assert fix_instructions_brute_force(test_data) == 8

input = get_data(day=8)
data = [line for line in input.splitlines()]

print(f"part A answer: {detect_cycle(data)}")
print(f"part B answer: {fix_instructions_brute_force(data)}")
