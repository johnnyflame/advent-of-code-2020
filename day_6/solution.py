from collections import Counter

from aocd import get_data


def count_questions(input):
    total_len = 0
    accum = set()
    for line in input.splitlines():
        if line == "":
            total_len += len(accum)
            accum = set()
        else:
            for ch in line:
                accum.add(ch)
    total_len += len(accum)
    return total_len


def count_question_2(input):
    total_count = 0
    ans = []
    intersect = set()

    for line in input.splitlines():
        if line == "":
            if not ans:
                continue
            elif len(ans) == 1:
                total_count += len(ans[0])
            else:
                intersect = set(ans[0])
                for other in ans[1:]:
                    intersect = intersect.intersection(other)
                total_count += len(intersect)
            ans = []
        else:
            ans.append(line)
            # intersect = set(line).intersection(intersect)
    total_count += len(ans)
    return total_count


test_data = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

assert count_questions(test_data) == 11
assert count_question_2(test_data) == 6

data = get_data(day=6)
print(f"Part A answer: {count_questions(data)}")
print(f"Part B answer: {count_question_2(data)}")

print("Done")
