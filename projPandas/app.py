"""
    ToDos for this project ¶
        1. Remove NaN values and change it to 0
        2. Make Roll_number column as index
        3. Sort Index
        4. Make new dataframe which consists of Only [Name, Score, Std]
        5. Save new dataframe as CSV
"""
import pandas as pd 

subject = "geography"

df = pd.read_csv(f'data/{subject}.csv', header=0)
df.rename(columns={'Roll no': 'Roll_number'}, inplace=True)


def main(df):
    df['Roll_number'] = df['Roll_number'].fillna(0)
    df['Roll_number'] = df['Roll_number'].astype(int)
    df.set_index('Roll_number', inplace=True)
    df = df.sort_index()
    main_df = df[['Name', 'Total score', 'Standard']]
    main_df.to_csv(f'toSend/ToSend{subject}Result.csv')

main(df)