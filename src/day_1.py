from aocd import get_data


def two_sum(input, target_sum):
    lookup = set()
    for val in input:
        if target_sum - val in lookup:
            return val * target_sum - val
        else:
            lookup.add(val)
    return None


def three_sum(input, target_sum):
    input = set(input)
    for val in input:
        new_target_sum = target_sum - val
        lookup = set()
        for other in input - {val}:
            if new_target_sum - other in lookup:
                return val * other * (new_target_sum - other)
            else:
                lookup.add(other)
    return None


def parse_numbers(input_data):
    output = []
    for line in input_data.splitlines():
        output.append(int(line))
    return output


if __name__ == "__main__":
    data = get_data(day=1)
    input_values = parse_numbers(data)
    print(f"answer to part 1: {two_sum(input_values, 2020)}")
    print(f"answer to part 2: {three_sum(input_values, 2020)}")
