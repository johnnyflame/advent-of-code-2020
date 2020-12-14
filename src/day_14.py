from aocd import get_data


def apply_bit_mask(mask, number):
    """
    Takes a 36-bit bitmask and applies a to a value
    """
    print(f"applying bitmask {mask} to number: {number}")

    bin_number = list(format(number, "036b"))
    for i, bit in enumerate(mask):
        if bit == "X":
            continue
        bin_number[i] = bit

    return int("".join(bin_number), 2)


def part_1(data):
    # use a dict to store the addresses
    mem_address = {}
    current_bit_mask = None
    for line in data.splitlines():
        if line[:4] == "mask":
            current_bit_mask = line.split()[2]
        elif line[:3] == "mem":
            key = int(line.split()[0][4:-1])
            original_value = int(line.split()[-1])
            mem_address[key] = apply_bit_mask(current_bit_mask, original_value)
        else:
            raise ValueError("Input needs to be either mask or a mem address of values")
    return sum(mem_address.values())


print(f"part 1: {part_1(get_data(day=14))}")
