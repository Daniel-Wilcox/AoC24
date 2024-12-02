# Advent of Code 2024

This year I have decided to participate in the [Advent of Code](https://adventofcode.com/2024/about) challenge. I'll attempt to be consistent throughout the challenges, despite missing the first day 🫠. 

# Stats

| Day # | Start | End | Time Taken |
| ----- | ----- | ----- | ----- |
| 1     |       |       |       | 
| 2     |       |       |       | 
| X     |       |       |       | 

# Helper scripts

## Initialize day's folders and files
I've created a script called [generate_project_day.py](./generate_project_day.py) which can be ran in a CLI to provide a basic initialization for the day's challenge. Currently it just achieves the following:

- Create "Day_X" directory
- touch "day_X_puzzle.txt"
- touch "day_X_input.csv"
- create python file: "day_X.py"

where the "day_X.py" contains a basic initial script:

```python 
#Day_X/day_X.py
def part_1():
    pass
def part_2():
    pass

if __name__ == "__main__":
    part_1()
    # part_2()
```

To run this from the CLI, one can use the following command:

```bash
python generate_project_day.py 7
```

which will create the above mentioned folders and files for the 7th day. 



