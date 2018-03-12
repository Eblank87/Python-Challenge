DOB=str("01/06/1987") 

print(str(DOB))
month= DOB.split("/")[0]
print(month)
day= DOB.split("/")[1]
print(day)
year=DOB.split("/")[2]
print(year)

DOB_New = str(int(year))+"/"+str(int(month))+"/"+str(int(day))
print(DOB_New)