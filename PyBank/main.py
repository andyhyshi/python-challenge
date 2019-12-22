#dependencies

import os
import csv

#path to csvfile

csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#initializes the variables 
total_months = 0
total_amount =0
changes =[]
date_count = []
great_inc = 0
great_inc_month = 0
great_dec = 0
great_dec_month = 0

# Opens the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# calculating the total number of months and total amount
    prev_profit = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    great_inc = int(row[1])
    great_inc_month = row[0]

    for row in csvreader:
 
        total_months += 1
        total_amount = total_amount + int(row[1])

        # Calculate change from this month to previous month
        change = int(row[1]) - prev_profit
        changes.append(change)
        prev_profit = int(row[1])
        date_count.append(row[0])
        
        #calculating the greatest increase
        if int(row[1]) > great_inc:
            great_inc = int(row[1])
            great_inc_month = row[0]
            
        #calculating the greatest decrease
        if int(row[1]) < great_dec:
            great_dec = int(row[1])
            great_dec_month = row[0]  
      
    # calculates the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # print all values
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months: " + str(total_months))
    print("Total Amount: $" + str(total_amount))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: "+ str(great_inc_month),'($'+ str(max(changes))+')')
    print("Greatest Decrease in Profits: "+ str(great_dec_month), '($'+str(min(changes))+')')

    q = open("output.txt", "w")
    q.write("Financial Analysis\n")
    q.write("----------------------------\n")        
    q.write("Total Months: " + str(total_months) + "\n")
    q.write("Total: $" + str(total_amount) + "\n")
    q.write("Average Change: $" + str(format(average_change, '.2f')) + "\n")
    q.write("Greatest Increase in Profits: " + great_inc_month 
        + " ($" + str(max(changes)) + ")\n")
    q.write("Greatest Decrease in Profits: " + great_dec_month 
        + " ($" + str(min(changes)) + ")\n")
    q.close()