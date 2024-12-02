import pandas as pd 


def _strictly_ascending(x: list) -> bool:

    len_x = len(x)
    if not len_x:
        return False
    
    if len_x > 1:
        return all(before < after for before, after in zip(x, x[1:]))

    return True



def check_requirement_1(x: list) -> bool:
    """The levels are either all increasing or all decreasing."""
    
    # Check strictly ascending
    if _strictly_ascending(x):
        return True
    
    # Check strictly descending
    x.reverse()
    if _strictly_ascending(x):
        return True
    
    return False

    

def check_requirement_2(x: list, min_diff:int = 1, max_diff:int=3) -> bool:
    """Any two adjacent levels differ by at least one and at most three."""

    len_x = len(x)
    if not len_x:
        return False
    
    difference_list = [abs(after - before) for before, after in zip(x, x[1:])]

    return all([True if (i >= min_diff) and (i <= max_diff) else False for i in difference_list])
    


def part_1():
    filepath = "Day_2/day_2_input.csv"
    num_safe = 0

    with open(filepath, "r+") as f:
        for idx, line in enumerate(f.readlines()):

            line_list = [int(i) for i in line.strip().split(",")]

            if not check_requirement_1(line_list):
                print(f"{idx}: {line_list} is unsafe (1)")
                continue

            if not check_requirement_2(line_list):
                print(f"{idx}: {line_list} is unsafe (2)")
                continue
            
            num_safe += 1

            print(f"{idx}: {line_list} is Safe")

    print(f"{num_safe}") #379
            
    # df = pd.read_csv(
    #     "Day_2/day_2_input.csv", 
    #     names=["a", "b", "c", "d", "e", "f", "g", "h"]
    # )

    # print(df.head())

def part_2():
    pass

if __name__ == "__main__":
    part_1()
    # part_2()
