import matplotlib.pyplot as plt
import seaborn as sns


def create_visualizations(df):

    # Revenue Chart
    plt.figure(figsize=(8, 5))
    sns.lineplot(x='Date', y='Revenue', data=df, marker='o')
    plt.title('Monthly Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visuals/revenue_chart.png')
    plt.show()

    # Profit Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Region', y='Profit', data=df)
    plt.title('Region Wise Profit')
    plt.tight_layout()
    plt.savefig('visuals/profit_chart.png')
    plt.show()

    # Expense Chart
    plt.figure(figsize=(8, 5))
    plt.pie(df['Expenses'], labels=df['Region'], autopct='%1.1f%%')
    plt.title('Expenses Distribution')
    plt.savefig('visuals/expense_chart.png')
    plt.show()
