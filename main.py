from src.data_cleaning import load_and_clean_data
from src.analysis import financial_summary
from src.visualization import create_visualizations


def main():
    file_path = 'data/financial_data.csv'

    # Load Data
    df = load_and_clean_data(file_path)

    # Show first rows
    print(df.head())

    # Analysis
    financial_summary(df)

    # Visualization
    create_visualizations(df)


if __name__ == '__main__':
    main()
