import pandas as pd

def main():

    df = pd.read_csv("Day_1/day_1_input.csv", header=None)
    print(df.head())
    pass

if __name__ == "__main__":
    main()
