import pytest
from src.day_18 import evaluate, evaluate_line, evaluate_part_2


class Test_day_18:
    def test_evaluate(self):
        test_input = "1 + 2 * 3 + 4 * 5 + 6"
        assert evaluate_line(test_input, evaluate) == 71

    def test_part_1_bracket(self):
        test_input = "1 + (2 * 3) + (4 * (5 + 6))"
        assert evaluate_line(test_input, evaluate) == 51

        test_input = "2 * 3 + (4 * 5)"
        assert evaluate_line(test_input, evaluate) == 26

    def part_2_tests(self):
        test_input = "1 + (2 * 3) + (4 * (5 + 6))"
        assert evaluate_line(test_input, evaluate_part_2) == 51
