#import csv files of polling data
import os
import csv




#grab polling CSVs
votecsv = os.path.join("PythonHW","Python-Challenge","election_data_" + sets + ".csv")
    
#create new CSV
new_vote_data_csv= os.path.join("PythonHW","Python-Challenge","election_data_" + sets + ".csv")

#open  CSV
with open(csvpath, newline="") as csvfile:
       csvreader = csv.reader(csvfile, delimiter=",")
       
        Candidate_List =[]
        unique_candidate = []
        for i in candidate:
        if i not in unique_candidate:
       unique_candidate.append(i)
        print(Candidate_List)
       #skip headers
       next(csvreader, None)
       for row in csvreader:
        total_votes_count= 0

       
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