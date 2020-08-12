#Bank informaton analysis

#Dependencies
import os
import csv

#Resources path definition
csvpath = os.path.join('Resources', 'budget_data.csv')

#Reading CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Removing the header
    csv_header = next(csvreader)    
    month_num = 0
    total_amount = 0
    greatest_inc = 0
    greatest_dec = 0
    month_inc =''
    month_dec =''
    

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        # Calculate the total number of months included in the dataset
        month_num += 1
        # The net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])
        
        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            month_inc = row[0]
        #The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            month_dec = row[0]

#Final results to the terminal
print(f"Total Months: {month_num}")
print(f"Total Amount: ${total_amount}")
print(f"Average Change: ${round(total_amount/month_num,2)}")

print(f"Greatest Increase in Profit: {month_inc} $({greatest_inc})")
print(f"Greatest Decrease in Profit: {month_dec} $({greatest_dec})")

final_results = [["Total Months:",month_num],
                 ["Total Amount:","$"+str(total_amount)],
                 ["Average Change:","$"+str(round(total_amount/month_num,2))],
                 ["Greatest Increase in Profit:",month_inc + " ($" + str(greatest_inc)+")"],
                 ["Greatest Decrease in Profit:",month_dec + " ($" + str(greatest_dec)+")"]]

#Final results to the CSV file
# Set variable for output file
output_file = os.path.join("analysis","Financial_Analysis.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------------"])

    # Write the list of results
    writer.writerows(final_results)
