import os
import csv

def fin_analysis(budget_csv):
    
    print(result_rows)
    
    

#-------------------------------------------------------
budget_csv = os.path.join("Resources", "budget_data.csv")
#Read in the CSV file:
with open(budget_csv, 'r', newline="") as csvfile_object:
    csvreader = csv.reader(csvfile_object, delimiter=",")
    print(type(csvreader))
    header = next(csvreader)
    #Print the Header row
    print(f'\n{header}')
    total = 0
    month_count = 0
    #Initiate an empty list to hold the integers for Profit/Losses:
    numbers = []
    
    #For each row in the csv file, print the data and the running total:
    for row in csvreader:
        i = int(row[1])
        print(f'{row[0]} |  {i}')
        total = total + (int(row[1]))
        month_count += 1
        numbers.append(i)
        
    #Calculate greatest incr and decr:
    greatest_incr = max(numbers)
    greatest_decr = min(numbers)
    end = sum(numbers)
    initial_value = numbers[0]
    ending_value = numbers[-1]
    avg_change_long = ((ending_value - initial_value)/ending_value)    
    avg_change = round(avg_change_long, 2)           
    print(f'\nTotal Net Profits/Losses = ${total}\n')  
    print(f'Total Number of Months: {month_count}\n')    
    print(f'The greatest increase was ${greatest_incr}\n')
    print(f'The greatest decrease was ${greatest_decr}\n')
    print(f'The percentage change over the time period was {avg_change}%.')
    
result_header = ['Financial Analysis\n+ + + + + + + + + + + + + + + + +\n']
result_rows = [
    "\nTotal Net Profits/Losses = ${total}\n",  
    "Total Number of Months: {month_count}\n",    
    "The greatest increase was ${greatest_incr}\n",
    "The greatest decrease was ${greatest_decr}\n"
        ]

#-------------------------------------------------------------------------

output_file = os.path.join("Resources", "new.csv")

with open(output_file, 'w') as file_object:
    csvwriter = csv.writer(file_object)    
    csvwriter.writerow(result_header)
    csvwriter.writerows(result_rows)
   