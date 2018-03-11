#import csv files of polling data
import os
import csv

#set paths for files
csvpath1 = os.path.join("PythonHW","Python-Challenge","election_data_1.csv")
csvpath2 = os.path.join("PythonHW","Python-Challenge","election_data_2.csv")

#open each CSV
with open(csvpath1, newline="" as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
with open(csvpath2, newline="" as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    