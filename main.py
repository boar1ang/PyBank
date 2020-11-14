import os
import csv
import sys 
#-------------------------------------------------------
budget_csv = os.path.join("Resources", "budget_data.csv")
#Read in the CSV file:
with open(budget_csv, 'r', newline="") as csvfile_object:
    csvreader = csv.reader(csvfile_object, delimiter=",")
    #print(type(csvreader))
    header = next(csvreader)
    #Print the Header row
    print(f'\n{header}')
    #Set total to 0 prior to calculations:
    total = 0
    #Set months of data to 0 before counting:
    month_count = 0
    #Initiate an empty list for the dates
    dates = []
    #Initiate an empty list to hold the integer values for Profit/Losses:
    numbers = []
    
    #For each row in the csv file, print the data and the running total:
    for row in csvreader:
        d = (row[0])
        i = int(row[1])
        print(f'{row[0]} |  {i}')
        total = total + (int(row[1]))
        month_count += 1
        dates.append(d)
        numbers.append(i)
        
    #Calculate greatest incr and decr:
    greatest_incr = max(numbers)
    dateIndexIncrPos = (numbers.index(greatest_incr))
    incr_date = dates[dateIndexIncrPos]
    
    greatest_decr = min(numbers)
    dateIndexDecrPos = numbers.index(greatest_decr)
    decr_date = dates[dateIndexDecrPos]

    end = sum(numbers)
    initial_value = numbers[0]
    ending_value = numbers[-1]
    avg_change_long = ((ending_value - initial_value)/ending_value)    
    avg_change = round(avg_change_long, 2)           
    
    print(f'\nFinancial Analysis\n+ + + + + + + + + + + + + + + + +\n')
    print(f'\nTotal Net Profits/Losses = ${total}\n')  
    print(f'Total Number of Months: {month_count}\n')    
    print(f'The greatest increase was ${greatest_incr} during {incr_date}\n')
    print(f'The greatest decrease was ${greatest_decr} during {decr_date}\n')
    print(f'The percentage change over the time period was {avg_change}%.\n')  

#-------------------------------------------------------------------------

output_file = os.path.join("Resources", "new.txt")

with open(output_file, 'w') as file_object:
    file_object.write(f'This message will be displayed on the screen:\n')
    
    print(f'\n+ + + + + + + + + + + + + + + + +\nFinancial Analysis\n+ + + + + + + + + + + + + + + + +\n', file = file_object)
    print(f'\nTotal Net Profits/Losses = ${total}\n', file = file_object)  
    print(f'Total Number of Months: {month_count}\n', file = file_object)    
    print(f'The greatest increase was ${greatest_incr} during {incr_date}\n', file = file_object)
    print(f'The greatest decrease was ${greatest_decr} during {decr_date}\n', file = file_object)
    print(f'The percentage change over the time period was {avg_change}%.\n', file = file_object)   