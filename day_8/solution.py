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


"""
How to approach it?

What if we just put it in a list, and keep track of the visited index in a set? 

"""


def detect_instruction_loop(instructions):
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
    has_cycle, accum = detect_instruction_loop(instructions)
    if has_cycle:
        options = {"jmp", "acc"}
        for i, line in enumerate(instructions):
            instruction, arg = line.split()
            if instruction in options:
                instructions[i] = list(options - {instruction})[0] + " " + arg
                has_cycle, accum = detect_instruction_loop(instructions)
                if not has_cycle:
                    break
                else:
                    instructions[i] = "acc " + arg
                    accum = 0

    return accum


test_data = [line for line in test_input.splitlines()]
assert detect_instruction_loop(test_data) == (True, 5)
print(fix_instructions_brute_force(test_data))


input = get_data(day=8)
data = [line for line in input.splitlines()]


print(detect_instruction_loop(data))

abc = 123
