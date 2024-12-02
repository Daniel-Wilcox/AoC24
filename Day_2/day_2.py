def _strictly_ascending(x: list) -> bool:

    len_x = len(x)
    if not len_x:
        return False
    
    if len_x > 1:
        return all(before < after for before, after in zip(x, x[1:]))

    return True


def check_requirement_1(x: list) -> bool:
    """The levels are either all increasing or all decreasing."""
    temp = x.copy()
    # Check strictly ascending
    if _strictly_ascending(temp):
        return True
    
    # Check strictly descending
    temp.reverse()
    if _strictly_ascending(temp):
        return True
    
    return False

    
def check_requirement_2(x: list, min_diff:int = 1, max_diff:int=3) -> bool:
    """Any two adjacent levels differ by at least one and at most three."""

    len_x = len(x)
    if not len_x:
        return False
    
    difference_list = [abs(after - before) for before, after in zip(x, x[1:])]

    return all([True if (i >= min_diff) and (i <= max_diff) else False for i in difference_list])
    

def combined_requirements(x: list) -> bool:

    if not check_requirement_1(x):
        return False

    if not check_requirement_2(x):
        return False
    
    return True


def part_1():

    filepath = "Day_2/day_2_input.csv"

    with open(filepath, "r+") as f:

        full_list = [
            (idx, [int(i) for i in line.strip().split(",")]) 
            for idx, line in enumerate(f.readlines())
        ]

    full_list_safe = [
        (idx, line_list, combined_requirements(line_list))
        for idx, line_list in full_list
    ]

    counting = sum([v for _, _, v in full_list_safe])

    print(f"Total safe: {counting}")


def recheck_with_removed_element(x: list)->bool:

    return any([
        combined_requirements(x[:idx] + x[idx + 1:])
        for idx in range(len(x))
    ])


def part_2():

    filepath = "Day_2/day_2_input.csv"


    with open(filepath, "r+") as f:

        full_list = [
            (idx, [int(i) for i in line.strip().split(",")]) 
            for idx, line in enumerate(f.readlines())
        ]

    full_list_safe = [
        (idx, line_list, combined_requirements(line_list))
        for idx, line_list in full_list
    ]

    part_1_count = sum([v for _, _, v in full_list_safe])

    # Part 2 recheck
    only_unsafe = [
        (i, j) for (i, j, k) in full_list_safe if not k
    ]

    only_unsafe_rechecked = [
        (idx, line_list, recheck_with_removed_element(line_list)) 
        for idx, line_list in only_unsafe
    ]
    part_2_count = sum([v for _, _, v in only_unsafe_rechecked])

    print(f"{part_2_count = }") # 379 < X < 442?

    counting = part_1_count + part_2_count

    print(f"Total safe: {counting}") # 430


if __name__ == "__main__":
    # part_1()
    part_2()
