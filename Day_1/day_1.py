import pandas as pd

def main():

    df = pd.read_csv("Day_1/day_1_input.csv", header=None)
    df = df.rename(columns={0:"left_id", 1:"right_id"})
    
    left_df = df[["left_id"]].copy()
    left_df = left_df.sort_values(by="left_id", ascending=True).reset_index(drop=True)

    right_df = df[["right_id"]].copy()
    right_df = right_df.sort_values(by="right_id", ascending=True).reset_index(drop=True)

    combined_df = pd.concat([left_df, right_df], axis=1)

    combined_df["diff"] = abs(combined_df["left_id"] - combined_df["right_id"])

    print(combined_df.head())
    print(combined_df["diff"].sum())
    pass

if __name__ == "__main__":
    main()
