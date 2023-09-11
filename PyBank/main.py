import os
import csv

csvpath = "PyBank/Resources/budget_data.csv"

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""

changes = []

total_months = 0
net_total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    header = next(csvreader)

    previous_profit = None

    for r in csvreader:
        month = r[0]
        profit = int(r[1])
        if previous_profit is not None:
            profit_increase = profit - previous_profit
            changes.append(profit_increase)
            if profit_increase > greatest_increase:
                greatest_increase = profit_increase
                greatest_increase_month = month
            if profit_increase < greatest_decrease:
                greatest_decrease = profit_increase
                greatest_decrease_month = month

        previous_profit = profit

        total_months +=1
        net = float(r[1])
        net_total += net
    average_profit = sum(changes)/len(changes)
    print(average_profit)
    print(greatest_decrease)

    print(f"Total number of months: {total_months}")
    print(f"Net total is {net_total}")
    print(f"The greatest increase in profits was {greatest_increase} in {greatest_increase_month}")
    print(f"The greatest decrease in profits was {greatest_decrease} in {greatest_decrease_month}")
    print(f"The average change in profit was {average_profit}")
