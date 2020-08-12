#Polling Station

#Dependencies
import os
import csv

#Resources path definition
csvpath = os.path.join('Resources', 'election_data.csv')

# Varibles
total_votes = 0

candidates = []
unique_candidates = []

winner = ''
winnerVotes = 0

#Reading CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Removing the header
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        # Calculate the total number of votes cast
        total_votes += 1
        # List of candidates who received votes
        candidates.append(row[2])

# Analysis 

# Function to count the votes
def countVotes(votesList, who):
    count = 0
    for votes in votesList:
        if (votes == who):
            count += 1
    return count        
# Extracting the unique list of candidates
for candidate in candidates:
    # check if exist in unique list of candidates
    if candidate not in unique_candidates:
        unique_candidates.append(candidate)

#Final results to the terminal
print(f"Election Results")
print(f"-----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------------")
for candidate in unique_candidates:
    
    sumVotes = countVotes(candidates,candidate)
    
    print(f"{candidate}: {round((sumVotes/total_votes) * 100,3)}% ({sumVotes})")
    if sumVotes >= winnerVotes:
        winnerVotes = sumVotes
        winner = candidate
    sumVotes = 0

print(f"-----------------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------------")

#Final results to the CSV file
# Set variable for output file
output_file = os.path.join("analysis","Poll_Analysis.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------------"])
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["-----------------------------------"])

    for candidate in unique_candidates:
        
        sumVotes = countVotes(candidates,candidate)
        
        writer.writerow([candidate + ": " + str(round((sumVotes/total_votes)*100,3)) + "% (" + str(sumVotes) +")"])
        if sumVotes >= winnerVotes:
            winnerVotes = sumVotes
            winner = candidate
        sumVotes = 0

    writer.writerow(["-----------------------------------"])
    writer.writerow(["Winner: " + winner])
    writer.writerow(["-----------------------------------"])
