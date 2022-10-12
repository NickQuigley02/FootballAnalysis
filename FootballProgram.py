##COURTESY OF GEEKS FOR GEEKS
# importing csv module
import csv
 
# csv file name
filename = "FootballData/MasterFootballData.txt"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    print((int)(row[7].split(" ")[1])) ##Primarily testing right here, casting a split of this to an int to test out how to make location a workable int.
    if((int)(row[7].split(" ")[1]) == 50):
        print((int)(row[7].split(" ")[1]))
    elif(row[1] == "Seahawks" and (row[7].split(" ")[0]) == "SEA"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    elif (row[1] == "Seahawks" and (row[7].split(" ")[0]) != "SEA"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Packers" and (row[7].split(" ")[0]) == "GNB"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    elif (row[1] == "Packers" and (row[7].split(" ")[0]) != "GNB"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bills" and (row[7].split(" ")[0]) == "BUF"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    elif (row[1] == "Bills" and (row[7].split(" ")[0]) != "BUF"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Cardinals" and (row[7].split(" ")[0]) == "CRD"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    elif (row[1] == "Cardinals" and (row[7].split(" ")[0]) != "CRD"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Saints" and (row[7].split(" ")[0]) == "NOR"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    elif (row[1] == "Saints" and (row[7].split(" ")[0]) != "NOR"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    
    for col in row:
        print("%10s"%col,end=" "),
        
    print('\n')
## COURTESY OF GEEKS FOR GEEKS    
for col in rows[5000]:
    print("%10s"%col,end=" "),
print("\n\n\n")
print(row[7].split(" "))
    

#For future reference
    #I have to find a way to convert something like "NEW 45" to an int based on whose playing the ball.
    #This can be done with just 32 if else,
    #if tm = HOME TEAM && if (Split the location into locTeam and locValue) locTeam != "HMT", locValue += 50;
    
