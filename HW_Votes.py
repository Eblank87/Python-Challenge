#import csv files of polling data
import os
import csv



#loop through data sets
for sets in datasets:
    #grab polling CSVs
    votecsv = os.path.join("PythonHW","Python-Challenge","election_data_" + sets + ".csv")
    
    #create new CSV
    new_vote_data_csv= os.path.join("PythonHW","Python-Challenge","election_data_" + sets + ".csv")
    #set new columns
    Voter_ID[]
    County[]
    Candidate[]
    
#open each CSV
    with open(csvpath, encoding="utf-8" as csvfile:
       csvreader = csv.reader(csvfile, delimiter=",")
       
       #skip headers
       next(csvreader, None)
       for row in  

Candidate_List =[]
Candidate_Votes= 
Winner = 

#show results
print("Election Results")
print("--------------------")
print("Total Votes: " + str(int(total_votes))
print("--------------------")
#list of candidates with votes/%
print("--------------------")
print("Winner: "+ str(winner))
print("--------------------")