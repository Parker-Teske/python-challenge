import os
import csv

# Path to collect data from Resources folder
budget_csv = os.path.join('C:/Users/ptesk/python-challenge/PyBank/Resourses/budget_data.csv')

# Create text file
output = os.path.join('pybank.txt')

total = 0 
month_change = []
profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000000]
total_loss = 0
# Read into csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Getting past headers
    header = next(csvreader)
    first = next(csvreader)
    total += 1
    total_loss += int(first[1])
    net_change1 = int(first[1])


# Starting loop
    for row in csvreader:
        total +=1 

     # Adding first object in total
        total_loss += int(row[1])

    # Net change
        net_change2 = int(row[1]) - net_change1 
        net_change1 = int(row[1])
        profit_loss += [net_change2]
        month_change += [row[0]]
        

    # Caluclating the greatest decrease
        if net_change2 <greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change2

    # Calculating the greatest increase
        if net_change2 > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change2
# Calculating the average net change
average_month = sum(profit_loss)/len(profit_loss)

# Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total}\n"
    f"Total: ${total_loss}\n"
    f"Average Change: {average_month:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

# Write into final file
f = open("pybank.txt", "w")
f.write(output)
f.close()
    
  
    
    
    
            

    
    
       





