import os
import csv

budgetdata = os.path.join('..', 'pychallenge', 'Python_budget_data.csv')

totalmonths = 0
netamount = 0
averageprct = 0
greatestincr = 0
greatestdecr = 0

prev_total = 0
change_list = []

with open(budgetdata, 'r') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')

    header = next(csvreader)
    

    for row in csvreader:
        totalmonths += 1 
        netamount += int(row[1])

        
        if totalmonths <= 1:
            difference = 0
        else:
            difference = int(row[1]) - prev_total
            change_list.append(difference)
        prev_total = int(row[1])

        


    averageprct = int(sum(change_list) / len(change_list))
    greatestincr = int(max(change_list))
    greatestdecr = int(min(change_list))

    print("Finacial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Net Total: ${netamount}")
    print(f"Average Change: ${averageprct}")
    print(f"Greatest increase in profits: ${greatestincr}")
    print(f"Greatest decrease in profits: ${greatestdecr}")




    
    