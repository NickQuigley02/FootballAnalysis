##This program was made by Nicholas Quigley
## to Analyze 4th-down plays in the 21st century of the NFL
## using data from Pro-football Reference.


import csv
import math
from team_names import team_abr ##This dictionary is responsible for checking the team name to the team abbreviation to turn the location from TEA XX format to an int between 1 and 100.

 
# csv file name
filename = "FootballData/MasterFootballData.txt"

# csv writing name
writename = "FootballData/ImprovedFootballData.txt"
 
# initializing the titles and rows list
fields = []
rows = []

## Same as above but for the file we're writing too
data = [] ## It'll have 15, the array 0-13 and then the power rankings.

f = open(writename, 'w')
writer = csv.writer(f)

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
    data.append(fields)
    data.append("Courage Index")
    data.append("Yards From Goalline")
    writer.writerow(data)
    data.clear()
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    fieldPosition = []
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
i = int ##This is the variable I am using for fieldPosition.
j = 0
timeRemaining = int ##This is the variable I am using for the time remaining in seconds.
scoreDiff = int ##This is what I use to keep track of the score in a single int.
courageIndex = float ##THAT GRANDEST OF VALUES!
for row in rows[:30000]:
    teamnamesFromTeamAbr = row[1]
    abbrFromTeamAbr = row[7].split(" ")[0];
    # parsing each column of a row
    if((row[7].split(" ")[0]) == "50"): ##Look into Dictionary-------------------------------------------- 
        i = ((int)(row[7].split(" ")[0])) ##This checks to see if the ball was at the 50, and thus in neither teams territory.
    elif(abbrFromTeamAbr == team_abr[teamnamesFromTeamAbr]):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)
    else:
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    ##print(team_abr[teamnamesFromTeamAbr],abbrFromTeamAbr)


     ##This is the bit that's gonna get the time total
    timeRemaining = ((((int)(row[3])-1)*15)*60) ##This is the quarter, minus 1 since comps start at 0, then multiply by 15 for the minutes and 60 for the seconds.
    timeRemaining += (15*60) - ((int)(row[4].split(":")[0]) * 60) + ((int)(row[4].split(":")[1])) #This adds on minutes in the quarter*60 to convert to seconds, then seconds.

    ##This is the bit that's gonna get the scoreDiff, or the difference between the two scores.
    scoreDiff = ((int)(row[8].split("-")[0])-(int)(row[8].split("-")[1]))

    ##HERE WE COMPUTE THY GRAND VALUE: THE INDEX OF 4TH DOWN COURAGE!
    
    courageIndex = 3 * math.log((int)(row[6])+1) ##Considers yards to go
    courageIndex *= 11+(10*math.cos(i/50 + math.pi/2)) ##Considers field position
    courageIndex *= ((70*60) - timeRemaining)/20 ##Subtracts the time from the overtime value of the game.
    if(scoreDiff < -7):
        courageIndex *= 1
    elif(scoreDiff < -3):
        courageIndex *= 1.5
    elif(scoreDiff < 0):
        courageIndex*= 2
    elif(scoreDiff == 0):
        courageIndex*= 2.5
    elif(scoreDiff <= 3):
        courageIndex*= 1.5
    elif(scoreDiff <= 7):
        courageIndex*= 0.75
    else:
        courageIndex*= 0.2
        
    ##for col in row:
    ##    print("%10s"%col,end=" "), ##If you want to see the rows print, uncomment this.
    ##print(i)
    ##print(timeRemaining)
    ##print(scoreDiff)
    ##print(courageIndex)

    
    for col in row:
        data.append(col)##This just causes every time to add to the data, so it just writes data [1] then data[1] and data[2] then data [1] and data[2] and data[3]
    data.append(courageIndex)
    data.append(i)
    writer.writerow(data)
    data.clear()



        
    #print('\n')
## COURTESY OF GEEKS FOR GEEKS    
for col in rows[5000]:
    print("%10s"%col,end=" "),
f.close()  

#For future reference
    #I have to find a way to convert something like "NEW 45" to an int based on whose playing the ball.
    #This can be done with just 32 if else,
    #if tm = HOME TEAM && if (Split the location into locTeam and locValue) locTeam != "HMT", locValue += 50;
    ##[8]
