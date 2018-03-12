import os
import csv

#employeedata_csv = os.path.join("LearnPython/Python-Challenge/employee_data_1.csv")
# Set empty list variables
Emp_ID = []
Name = []
DOB = []
SSN = []
State = []
#open current csv
with open('employee_data1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
#skip headers
    #next(csvReader,None)
    next(csvreader,None)
    for row in csvreader:
#append data from the row
        Emp_ID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])


#split Name into Last and First Name
Last_Name = [i.split(' ', 1)[1] for i in Name]
First_Name = [i.split(' ', 1)[0] for i in Name]

#convert date from yyyy-mm-dd to mm/dd/yyyy
for i in DOB:
    Year= [i.split("-",1)][0]
    Month = [i.split('-', 1)][0]
    Day = [i.split('-', 1)][0]     
DOB_New = str(Month)+"/"+str(Day)+"/"+str(Year)

SSN_New = str("***-**-"+(int(SSN.split("-",[2])))
#convert State Name into State Abreviation by looking up abr in dictionary

state_final = [] 
    State_abr = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR', 'California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID', 'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS', 'Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT', 'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT', 'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI', 'Wyoming': 'WY',}

for i in State_abr:
    for k,v in State_abr.items():
        if i == k:
            State_abr.append(v)
print(state_final) 

#zip lists together
    cleancsv = zip(Emp_ID, First_Name, Last_Name, DOB_New, SSN, State_Final)
   

newemployeecsv = os.path.join('newemployee_data_1.csv')              
with open('newemployee_data_1.csv',"w",newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
#write new headers
    csvwriter.writerow(["Emp_ID","Last Name","First Name","DOB_New", "SSN", "State"])

    csvwriter.writerows(cleancsv)