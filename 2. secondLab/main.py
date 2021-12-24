import pandas as pd
import numpy as np


def print_task(number):
    print(f'\n\n\n--------------------------\n\t\t\t{number}\n--------------------------\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # setting global printing options.
    pd.set_option('display.max_columns', None)

    # task 1.
    print_task(1)
    csv = pd.read_csv("data.csv", delimiter=',')
    print(csv)
    print("all cols:\n", csv.columns.values)

    # task 2.
    print_task(2)
    print(csv.describe())

    # task 3.
    print_task(3)
    print("head(3):\n", csv.head(3), "\ntail(7):\n", csv.tail(7))

    # task 4.
    print_task(4)
    print("Read .txt file with col name's desc.\n\tDone.")

    # task 5.
    print_task(5)
    i = csv['MonthlyIncome'] > 0
    new_csv = csv.loc[i, 'MonthlyIncome']
    csv['DebtRatio'] = csv['DebtRatio'] * new_csv
    print(new_csv.tail(7))
    print(csv.head())

    # task 6.
    print_task(6)
    csv.rename(columns={'DebtRatio': 'Debt'}, inplace=True)
    print(csv.head())

    # task 7.
    print_task(7)
    monthly_income_mean = csv['MonthlyIncome'].mean()
    csv['MonthlyIncome'] = csv['MonthlyIncome'].replace(np.nan, monthly_income_mean)
    print(csv.tail(7))

    # task 8.
    print_task(8)
    prob_with_dependents = (csv['SeriousDlqin2yrs'] == 1)\
        .groupby(csv['NumberOfDependents']).mean()
    prob_with_loans_and_lines = (csv['SeriousDlqin2yrs'] == 1)\
        .groupby(csv['NumberRealEstateLoansOrLines']).mean()
    print("probability with amount of dependents:\n", prob_with_dependents)
    print("\n\n\nprobability with amount of real loans and lines:\n", prob_with_loans_and_lines)
