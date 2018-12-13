import os
import csv

votedata = os.path.join('Python_election_data.csv')

totalvotes = 0
candidates = 0
candidatelist = []

with open(votedata, 'r') as votefile:
    csvreader = csv.reader(votefile, delimiter=',')

    header = next(csvreader)
    print(header)

    for row in csvreader:
        totalvotes += 1 
        winPercent = (int(row[0]) / totalvotes) * 100
        candidatelist.append([row[2], winPercent])
              
    print("Election Results")
    print("--------------------------------------")
    print(f"{totalvotes}")
    print("--------------------------------------")
    print(f"")
   

        


    
   