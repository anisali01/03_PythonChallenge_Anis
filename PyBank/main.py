# PyBank Homework by Anis Ali

import csv
import os

#Locate the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Set variables
months = []
amounts = []
change = []
changeMonth = []

count = 0

#Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip header
    csv_header = next(csvfile)

    #Read file
    for row in csv.reader(csvfile):

        #First time through set the newAmount for calculation
        if count == 0:
            #add 1 for first pass only
            count = count + 1
            #set amount for future calculations
            newAmount = int(row[1])
            #add amounts to amount list
            amounts.append(int(row[1]))
            #add months to month list
            months.append(str(row[0]))
        else:
            #add amounts to amount list
            amounts.append(int(row[1]))
            #add months to month list
            months.append(str(row[0]))
            #calculate change
            change.append(int(int(row[1]) - newAmount))
            #append change month
            changeMonth.append(str(row[0]))
            #set new amount for next row
            newAmount = int(row[1])

    #calculate results based on for loop entries
    totalMonths = len(months)
    totalAmount = sum(amounts)
    averageChange = (sum(change) / len(changeMonth))
    maxChange = max(change)
    maxChangeMonthIndex = change.index(maxChange)
    minChange = min(change)
    minChangeMonthIndex = change.index(minChange)

#Terminal Results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: $ {totalAmount}')
print(f'Average Change: $ {averageChange}')
print(f'Greatest Increase in Profits: {changeMonth[int(maxChangeMonthIndex)]} ($ {maxChange})')
print(f'Greatest Decrease in Profits: {changeMonth[int(minChangeMonthIndex)]} ($ {minChange})')

#Text Results
output_path = os.path.join("Analysis", "Financial Analysis.txt")
with open(output_path, "w", newline='') as datafile:
    print('Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {totalMonths}\n'
    f'Total: {totalAmount}\n'
    f'Average Change: {averageChange}\n'
    f'Greatest Increase in Profits: {changeMonth[int(maxChangeMonthIndex)]} ({maxChange})\n'
    f'Greatest Decrease in Profits: {changeMonth[int(minChangeMonthIndex)]} ({minChange})', file=datafile)
