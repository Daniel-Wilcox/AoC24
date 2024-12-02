import os
import argparse

def _touch_file(folder_name: str, file_name: str):
    file = os.path.join(folder_name, file_name)
    with open(file, 'w') as f:
        pass


def _create_python_file(folder_name: str, file_name: str):
    py_file = os.path.join(folder_name, file_name)
    with open(py_file, 'w') as f:
        f.write(
            f"""def part_1():\n    pass\n\ndef part_2():\n    pass\n\nif __name__ == "__main__":\n    part_1()\n    # part_2()\n"""
        )

def create_project_folder(day):
    folder_name = f"Day_{day}"
    
    # Creating folders and files
    os.makedirs(folder_name, exist_ok=True)
    _touch_file(folder_name, f"day_{day}_puzzle.txt")
    _touch_file(folder_name, f"day_{day}_input.csv")
    _create_python_file(folder_name, f"day_{day}.py")


if __name__ == "__main__":

    # Create the parser requirements
    parser = argparse.ArgumentParser()
    parser.add_argument('day', help="Day number to use for the project folder")    
    args = parser.parse_args()
    
    # Use the provided argument directly as the day variable
    day = args.day
    create_project_folder(day)

