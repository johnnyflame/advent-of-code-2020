import pytest
from src.day_8 import detect_cycle, fix_instructions_brute_force


class Test_day_8:
    def test_detect_cycle(self):
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

        test_data = [line for line in test_input.splitlines()]
        assert detect_cycle(test_data) == (True, 5)
