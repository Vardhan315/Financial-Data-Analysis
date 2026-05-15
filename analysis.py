def financial_summary(df):
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    total_profit = df['Profit'].sum()

    print("\n----- Financial Summary -----")
    print(f"Total Revenue  : {total_revenue}")
    print(f"Total Expenses : {total_expenses}")
    print(f"Total Profit   : {total_profit}")

    best_month = df.loc[df['Profit'].idxmax()]

    print("\nBest Profit Month:")
    print(best_month[['Date', 'Profit']])

    region_profit = df.groupby('Region')['Profit'].sum()

    print("\nRegion Wise Profit:")
    print(region_profit)
