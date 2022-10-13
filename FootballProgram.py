##COURTESY OF GEEKS FOR GEEKS
# importing csv module
import csv
import math
 
# csv file name
filename = "FootballData/MasterFootballData.txt"

# csv writing name
writename = "FootballData/ImprovedFootballData.txt"
 
# initializing the titles and rows list
fields = []
rows = []

## Same as above but for the file we're writing too
writeFields = []
writeRows = []

f = open(writename, 'w')
writer = csv.writer(f)

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
    fieldPosition = []
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
i = int ##This is the variable I am using for fieldPosition.
timeRemaining = int ##This is the variable I am using for the time remaining in seconds.
scoreDiff = int ##This is what I use to keep track of the score in a single int.
courageIndex = float ##THAT GRANDEST OF VALUES!
# printing first 5 rows
print('\nFirst 5 rows are:\n') ##WHAT IS BELOW YOU IS THE UGLIEST GODDAMN TESTING BIT YOU EVER DID SEE
for row in rows[:100]:
    # parsing each column of a row
    if((row[7].split(" ")[0]) == "50"):
        i = ((int)(row[7].split(" ")[0])) ##This checks to see if the ball was at the 50, and thus in neither teams territory.
    elif(row[1] == "Seahawks" and (row[7].split(" ")[0]) == "SEA"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           1 Theoretically, I could have done this with a switch case and some fucked up if statements. but screw it.
    elif (row[1] == "Seahawks" and (row[7].split(" ")[0]) != "SEA"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Packers" and (row[7].split(" ")[0]) == "GNB"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           2
    elif (row[1] == "Packers" and (row[7].split(" ")[0]) != "GNB"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bills" and (row[7].split(" ")[0]) == "BUF"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           3
    elif (row[1] == "Bills" and (row[7].split(" ")[0]) != "BUF"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Cardinals" and (row[7].split(" ")[0]) == "CRD"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           4
    elif (row[1] == "Cardinals" and (row[7].split(" ")[0]) != "CRD"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Saints" and (row[7].split(" ")[0]) == "NOR"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           5
    elif (row[1] == "Saints" and (row[7].split(" ")[0]) != "NOR"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Vikings" and (row[7].split(" ")[0]) == "MIN"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           6
    elif (row[1] == "Vikings" and (row[7].split(" ")[0]) != "MIN"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Dolphins" and (row[7].split(" ")[0]) == "MIA"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           7
    elif (row[1] == "Dolphins" and (row[7].split(" ")[0]) != "MIA"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Buccaneers" and (row[7].split(" ")[0]) == "TAM"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           8
    elif (row[1] == "Buccaneers" and (row[7].split(" ")[0]) != "TAM"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Browns" and (row[7].split(" ")[0]) == "CLE"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           9
    elif (row[1] == "Browns" and (row[7].split(" ")[0]) != "CLE"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Chiefs" and (row[7].split(" ")[0]) == "KAN"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           10
    elif (row[1] == "Chiefs" and (row[7].split(" ")[0]) != "KAN"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Panthers" and (row[7].split(" ")[0]) == "CAR"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           11
    elif (row[1] == "Panthers" and (row[7].split(" ")[0]) != "CAR"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Falcons" and (row[7].split(" ")[0]) == "ATL"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           12
    elif (row[1] == "Falcons" and (row[7].split(" ")[0]) != "ATL"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Steelers" and (row[7].split(" ")[0]) == "PIT"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           13
    elif (row[1] == "Steelers" and (row[7].split(" ")[0]) != "PIT"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bears" and (row[7].split(" ")[0]) == "CHI"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           14
    elif (row[1] == "Bears" and (row[7].split(" ")[0]) != "CHI"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Lions" and (row[7].split(" ")[0]) == "DET"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           15
    elif (row[1] == "Lions" and (row[7].split(" ")[0]) != "DET"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Colts" and (row[7].split(" ")[0]) == "CLT"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           16
    elif (row[1] == "Colts" and (row[7].split(" ")[0]) != "CLT"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "49ers" and (row[7].split(" ")[0]) == "SFO"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           17
    elif (row[1] == "49ers" and (row[7].split(" ")[0]) != "SFO"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Cowboys" and (row[7].split(" ")[0]) == "DAL"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           18
    elif (row[1] == "Cowboys" and (row[7].split(" ")[0]) != "DAL"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Washington" and (row[7].split(" ")[0]) == "WAS"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           19
    elif (row[1] == "Washington" and (row[7].split(" ")[0]) != "WAS"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bengals" and (row[7].split(" ")[0]) == "CIN"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           20
    elif (row[1] == "Bengals" and (row[7].split(" ")[0]) != "CIN"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Jaguars" and (row[7].split(" ")[0]) == "JAX"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           21
    elif (row[1] == "Jaguars" and (row[7].split(" ")[0]) != "JAX"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Eagles" and (row[7].split(" ")[0]) == "PHI"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           22
    elif (row[1] == "Eagles" and (row[7].split(" ")[0]) != "PHI"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Rams" and (row[7].split(" ")[0]) == "RAM"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           23
    elif (row[1] == "Rams" and (row[7].split(" ")[0]) != "RAM"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Giants" and (row[7].split(" ")[0]) == "NYG"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           24
    elif (row[1] == "Giants" and (row[7].split(" ")[0]) != "NYG"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Ravens" and (row[7].split(" ")[0]) == "RAV"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           25
    elif (row[1] == "Ravens" and (row[7].split(" ")[0]) != "RAV"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Chargers" and (row[7].split(" ")[0]) == "SDG"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           26
    elif (row[1] == "Chargers" and (row[7].split(" ")[0]) != "SDG"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Titans" and (row[7].split(" ")[0]) == "OTI"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           28
    elif (row[1] == "Titans" and (row[7].split(" ")[0]) != "OTI"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Patriots" and (row[7].split(" ")[0]) == "NWE"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           29
    elif (row[1] == "Patriots" and (row[7].split(" ")[0]) != "NWE"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Raiders" and (row[7].split(" ")[0]) == "RAI"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           30
    elif (row[1] == "Raiders" and (row[7].split(" ")[0]) != "RAI"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Texans" and (row[7].split(" ")[0]) == "HTX"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           31
    elif (row[1] == "Texans" and (row[7].split(" ")[0]) != "HTX"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Jets" and (row[7].split(" ")[0]) == "NYJ"):
        i = ((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           32
    elif (row[1] == "Jets" and (row[7].split(" ")[0]) != "NYJ"):
        i = (100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)

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
        
    for col in row:
        print("%10s"%col,end=" "),
    print(i)
    print(timeRemaining)
    print(scoreDiff)
    print(courageIndex)

        
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
    ##[8]
