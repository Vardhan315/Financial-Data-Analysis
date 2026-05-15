import pandas as pd


def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Remove null values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    return df
