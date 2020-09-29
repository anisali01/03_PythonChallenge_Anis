# PyPoll Homework by Anis Ali

import os
import csv

#Locate the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

#create dictionary for votes
votes = {}

#Read CSV
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip header 
    csv_header = next(csvfile)

    #Read file
    for row in csvreader:

        #Which column is the candidate
        candidate = row[2]

        #If candidate isn't present, create candidate
        if candidate not in votes:
            votes[candidate] = 1

        #If already in disctionary, give a vote
        else:
            votes[candidate] += 1

#Results
#Add the dictionary keys for totals
values = votes.values()
voteTotal = sum(values)

#Terminal Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {voteTotal}")
print(f"-------------------------")
for key, value in votes.items():
    print(f"{key}: {value / voteTotal:.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(votes, key=votes.get)}")
print(f"-------------------------")

#Text Results
output_path = os.path.join("Analysis", "Election Results.txt")
with open(output_path, "w", newline='') as datafile:
    datafile.write(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {voteTotal}\n"
    f"-------------------------\n")
    #note for loop has to be left out of datafile.write parenthesis to run
    for key, value in votes.items():
        #add a datafile.write line for results alone
        datafile.write(f"{key}: {value / voteTotal:.3%} ({value})\n")
    datafile.write(f"-------------------------\n"
    f"Winner: {max(votes, key=votes.get)}\n"
    f"-------------------------")