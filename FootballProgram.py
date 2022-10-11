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
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
## COURTESY OF GEEKS FOR GEEKS    
for col in rows[5000]:
    print("%10s"%col,end=" "),

#For future reference
    #I have to find a way to convert something like "NEW 45" to an int based on whose playing the ball.
    #This can be done with just 32 if else,
    #if tm = HOME TEAM && if (Split the location into locTeam and locValue) locTeam != "HMT", locValue += 50;
    
