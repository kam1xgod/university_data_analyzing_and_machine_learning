import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def print_task(number):
    print(f'\n\n\n--------------------------\n\t\t\t{number}\n--------------------------\n')


if __name__ == '__main__':

    # task 1
    csv = pd.read_csv("company_sales_data.csv")
    plt.figure()
    plt.plot(csv['month_number'], csv['total_profit'])
    plt.xlabel("Month number")
    plt.ylabel("Total profit")
    plt.title("Company profit per month")
    plt.show()

    # task 2.
    plt.figure()
    plt.plot(csv['month_number'], csv['total_units'],
             linestyle='--',
             color="r",
             label="Profit data of last year.",
             marker='o',
             markerfacecolor="black",
             markeredgecolor="red",
             linewidth=3)
    plt.xlabel("Month number")
    plt.ylabel("Total units")
    plt.legend("Profit data of last year")
    plt.title("Company sales data of last year")
    plt.show()

    # task 3.
    plt.figure()
    plt.plot(csv['month_number'], csv['facecream'],
             color="blue",
             label="Face cream sales data",
             marker='o',
             linewidth=3)

    plt.plot(csv['month_number'], csv['facewash'],
             color="orange",
             label="Face wash sales data",
             marker='o',
             linewidth=3)

    plt.plot(csv['month_number'], csv['toothpaste'],
             color="g",
             label="Tooth paste sales data",
             marker='o',
             linewidth=3)

    plt.plot(csv['month_number'], csv['bathingsoap'],
             color="r",
             label="Bathing soap sales data",
             marker='o',
             linewidth=3)

    plt.plot(csv['month_number'], csv['shampoo'],
             color="purple",
             label="Shampoo sales data",
             marker='o',
             linewidth=3)

    plt.plot(csv['month_number'], csv['moisturizer'],
             color="brown",
             label="Moisturizer sales data",
             marker='o',
             linewidth=3)

    plt.xlabel("Month number")
    plt.ylabel("Sales units in number")
    plt.legend()
    plt.title("Sales data")
    plt.show()

    # task 4.
    plt.figure()
    plt.scatter(csv['month_number'], csv['toothpaste'], label="Tooth paste Sales data")
    plt.xlabel("Month number")
    plt.ylabel("Number of units sold.")
    plt.legend()
    plt.title("Tooth paste sales data.")
    plt.show()

    # task 5.
    plt.figure()
    x1 = csv['facecream']
    x2 = csv['facewash']
    months = [csv['month_number'], csv['month_number']]
    label1 = "Face cream sales data"
    label2 = "Face wash sales data"
    plt.hist(months, weights=[x1, x2], label=label1)
    plt.legend()
    plt.xlabel("Month number")
    plt.ylabel("sales units in numbers")
    plt.title("face wash and face cream sales data.")
    plt.show()

    # task 6.
    plt.figure()
    plt.bar(csv['month_number'], csv['bathingsoap'])
    plt.title("Bathing soap sales data")
    plt.xlabel("Month number")
    plt.ylabel("sales units in numbers")
    plt.show()

    # task 7.
    plt.xlabel("profit range in dollar")
    plt.ylabel("Actual Profit in dollar")
    plt.title("Profit data")
    bot = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    plt.hist(csv["total_profit"], bins=bot)
    plt.legend({"Profit data"}, loc='upper left')
    plt.show()

    # task 8.
    names = [
        "Face cream",
        "Face wash",
        "ToothPaste",
        "Bathing Soap",
        "Shampoo",
        "Moisturizer",
    ]
    values = [
        csv["facecream"].sum(),
        csv["facewash"].sum(),
        csv["toothpaste"].sum(),
        csv["bathingsoap"].sum(),
        csv["shampoo"].sum(),
        csv["moisturizer"].sum()
    ]
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=names, autopct='%1.1f%%')
    leg = plt.legend(names, loc='lower right', bbox_to_anchor=(1.75, 0))
    plt.show()

    # task 9.
    fig1, (ax1, ax2) = plt.subplots(2, 1)
    ax2.plot(csv["month_number"], csv["facewash"], 'r-', lw=3, marker='o')
    ax2.set_title("Sales data of facewash")
    ax2.set_ylabel("Sales units in number")
    ax2.set_xlabel("Month Number")
    ax1.plot(csv["month_number"], csv["bathingsoap"], 'k-', lw=3, marker='o')
    ax1.set_title("Sales data of bathingsoap")
    ax1.xaxis.set_visible(False)
    plt.show()

    # task 10.
    y = np.vstack(
        [csv["facecream"], csv["facewash"], csv["toothpaste"], csv["bathingsoap"], csv["shampoo"], csv["moisturizer"]])
    plt.stackplot(csv["month_number"], y, colors=['purple', 'aqua', 'red', 'black', 'green', 'yellow'])
    plt.ylabel("Sales units in number")
    plt.xlabel("Month number")
    plt.title("Alll product sales data using stack plot")
    names = {
        "Face cream",
        "Face wash",
        "Toothpaste",
        "Bathing Soap",
        "Shampoo",
        "Moisturizer"
    }
    plt.legend(names, loc='upper left')
    plt.show()
