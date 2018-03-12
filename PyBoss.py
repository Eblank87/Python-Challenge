import os
import csv

employeedata_csv = os.path.join("LearnPython","PythonHW","Python-Challenge","employee_data_1.csv")

#create new CSV
newemployeecsv = os.path.join("LearnPython","PythonHW","Python-Challenge","newemployee_data_1.csv")

# Set empty list variables
Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []
#open current csv
with open(employeedata_csv, newline="") as csvfile:
    csvReader = csv.reader(csvFile,delimiter=',')
#skip headers
    next(csvReader,None)

for row in csvReader:
#append data from the row
Emp_ID.append(row[0])
Name.append(row[1])
DOB.append(row[2])
SSN.append(row[3])
State.append(row[4])

Last_Name = Name.split(' ')[1]
First_Name = Name.split(' ')[0]
DOB_New = str(int(DOB.split('/')[1])+"/"+int(DOB.split('/')[0])+"/"+int(DOB.split('/')[2]))
SSN_New = str("***-**-"+(int(SSN.split("-",[2])))
State_abr = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR', 'California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID', 'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS', 'Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT', 'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT', 'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI', 'Wyoming': 'WY',}

#zip lists together
    cleancsv = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)

    with open("newemployeedata.csv","w",newline="") as csvfile:
        csvwriter = csv.writer(csvFile, delimiter=',')
    
    #write headers into file
    csvwriter.writerrow(["Emp_ID","First_Name","Last_Name", "DOB_New", "SSN_New", "State_abr")
    ])
        #write the zipped list into a CSV
        csvwriter.writerows(cleancsv)