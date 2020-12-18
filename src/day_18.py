from collections import deque

from aocd.get import get_data


def evaluate(input):
    """
    evaluate a list of tokens and ops
    """
    input = list(input)
    accum = int(input[0])
    for op, token in zip(input[1:], input[2:]):
        if op == "*":
            accum *= int(token)
        elif op == "+":
            accum += int(token)
    return accum


def evaluate_part_2(input):
    stack = []
    queue = deque()
    for token in input:
        if token == "*":
            while stack and stack[-1] != "*":
                queue.appendleft(stack.pop())
            stack.append(evaluate(queue))
            stack.append(token)
            queue = deque()
        else:
            stack.append(token)

    while stack and stack[-1] != "*":
        queue.appendleft(stack.pop())
    stack.append(evaluate(queue))
    return evaluate(stack)


def evaluate_line(line, evaluator):
    stack = []
    queue = deque()
    for token in list(line.replace(" ", "")):
        if token == ")":
            while stack[-1] != "(":
                queue.appendleft(stack.pop())
            result = evaluator(queue)
            stack.pop()
            stack.append(result)
            queue = deque()
        else:
            stack.append(token)
    return evaluator(stack)


def sum_lines(input, evaluator):
    return sum(evaluate_line(line, evaluator) for line in input.splitlines())


print(f"part 1 : {sum_lines(get_data(day=18),evaluate)}")
print(f"part 2 : {sum_lines(get_data(day=18),evaluate_part_2)}")
