import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

def fin_analysis(budget_data):
    total_mos = int(len(csvreader))
    print(f'FINANCIAL ANALYSIS\n+  +  +  +  +  +  +  +  +  +  +')
    # print(f'Total Months: {total_mos}')
    print(f'Total Net Profits/Losses: {total}')
    # print(f'Average Change: {avg_change}')
    # print(f'Greatest Increase in Profits: {greatest_incr}')
    # print(f'Greatest Decrease in Profits: {greatest_decr}')

    
    
    # avg_change = 
    # greatest_incr = 
    # greatest_decr = 


# fin_analysis(total_mos)
with open(budget_csv, 'r', newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    header = next(csvreader)
    total = 0

    for row in csvreader:
        print(row)
        total = total + (int(row[1]))
        print(total)
fin_analysis(csvreader)
# output_path = os.path.join("Resources", "new.csv")
    
# with open(output_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter = ',')
#     csvwriter.writerow(fin_analysis(total))
