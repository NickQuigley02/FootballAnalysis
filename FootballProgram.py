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
    fieldPosition = []
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n') ##WHAT IS BELOW YOU IS THE UGLIEST GODDAMN TESTING BIT YOU EVER DID SEE
for row in rows[:100]:
    # parsing each column of a row
    if((row[7].split(" ")[0]) == "50"):
        print((int)(row[7].split(" ")[0])) ##This checks to see if the ball was at the 50, and thus in neither teams territory.
    elif(row[1] == "Seahawks" and (row[7].split(" ")[0]) == "SEA"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           1 Theoretically, I could have done this with a switch case and some fucked up if statements. but screw it.
    elif (row[1] == "Seahawks" and (row[7].split(" ")[0]) != "SEA"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Packers" and (row[7].split(" ")[0]) == "GNB"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           2
    elif (row[1] == "Packers" and (row[7].split(" ")[0]) != "GNB"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bills" and (row[7].split(" ")[0]) == "BUF"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           3
    elif (row[1] == "Bills" and (row[7].split(" ")[0]) != "BUF"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Cardinals" and (row[7].split(" ")[0]) == "CRD"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           4
    elif (row[1] == "Cardinals" and (row[7].split(" ")[0]) != "CRD"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Saints" and (row[7].split(" ")[0]) == "NOR"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           5
    elif (row[1] == "Saints" and (row[7].split(" ")[0]) != "NOR"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Vikings" and (row[7].split(" ")[0]) == "MIN"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           6
    elif (row[1] == "Vikings" and (row[7].split(" ")[0]) != "MIN"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Dolphins" and (row[7].split(" ")[0]) == "MIA"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           7
    elif (row[1] == "Dolphins" and (row[7].split(" ")[0]) != "MIA"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Buccaneers" and (row[7].split(" ")[0]) == "TAM"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           8
    elif (row[1] == "Buccaneers" and (row[7].split(" ")[0]) != "TAM"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Browns" and (row[7].split(" ")[0]) == "CLE"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           9
    elif (row[1] == "Browns" and (row[7].split(" ")[0]) != "CLE"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Chiefs" and (row[7].split(" ")[0]) == "KAN"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           10
    elif (row[1] == "Chiefs" and (row[7].split(" ")[0]) != "KAN"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Panthers" and (row[7].split(" ")[0]) == "CAR"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           11
    elif (row[1] == "Panthers" and (row[7].split(" ")[0]) != "CAR"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Falcons" and (row[7].split(" ")[0]) == "ATL"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           12
    elif (row[1] == "Falcons" and (row[7].split(" ")[0]) != "ATL"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Steelers" and (row[7].split(" ")[0]) == "PIT"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           13
    elif (row[1] == "Steelers" and (row[7].split(" ")[0]) != "PIT"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bears" and (row[7].split(" ")[0]) == "CHI"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           14
    elif (row[1] == "Bears" and (row[7].split(" ")[0]) != "CHI"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Lions" and (row[7].split(" ")[0]) == "DET"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           15
    elif (row[1] == "Lions" and (row[7].split(" ")[0]) != "DET"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Colts" and (row[7].split(" ")[0]) == "CLT"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           16
    elif (row[1] == "Colts" and (row[7].split(" ")[0]) != "CLT"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "49ers" and (row[7].split(" ")[0]) == "SFO"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           17
    elif (row[1] == "49ers" and (row[7].split(" ")[0]) != "SFO"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Cowboys" and (row[7].split(" ")[0]) == "DAL"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           18
    elif (row[1] == "Cowboys" and (row[7].split(" ")[0]) != "DAL"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Washington" and (row[7].split(" ")[0]) == "WAS"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           19
    elif (row[1] == "Washington" and (row[7].split(" ")[0]) != "WAS"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Bengals" and (row[7].split(" ")[0]) == "CIN"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           20
    elif (row[1] == "Bengals" and (row[7].split(" ")[0]) != "CIN"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Jaguars" and (row[7].split(" ")[0]) == "JAX"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           21
    elif (row[1] == "Jaguars" and (row[7].split(" ")[0]) != "JAX"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Eagles" and (row[7].split(" ")[0]) == "PHI"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           22
    elif (row[1] == "Eagles" and (row[7].split(" ")[0]) != "PHI"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Rams" and (row[7].split(" ")[0]) == "RAM"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           23
    elif (row[1] == "Rams" and (row[7].split(" ")[0]) != "RAM"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Giants" and (row[7].split(" ")[0]) == "NYG"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           24
    elif (row[1] == "Giants" and (row[7].split(" ")[0]) != "NYG"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Ravens" and (row[7].split(" ")[0]) == "RAV"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           25
    elif (row[1] == "Ravens" and (row[7].split(" ")[0]) != "RAV"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Chargers" and (row[7].split(" ")[0]) == "SDG"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           26
    elif (row[1] == "Chargers" and (row[7].split(" ")[0]) != "SDG"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Titans" and (row[7].split(" ")[0]) == "OTI"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           28
    elif (row[1] == "Titans" and (row[7].split(" ")[0]) != "OTI"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Patriots" and (row[7].split(" ")[0]) == "NWE"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           29
    elif (row[1] == "Patriots" and (row[7].split(" ")[0]) != "NWE"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Raiders" and (row[7].split(" ")[0]) == "RAI"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           30
    elif (row[1] == "Raiders" and (row[7].split(" ")[0]) != "RAI"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Texans" and (row[7].split(" ")[0]) == "HTX"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           31
    elif (row[1] == "Texans" and (row[7].split(" ")[0]) != "HTX"):
        print(100-(int)(row[7].split(" ")[1])) ##Representing a location closer to opp's endzone (100 - yardage)
    elif(row[1] == "Jets" and (row[7].split(" ")[0]) == "NYJ"):
        print((int)(row[7].split(" ")[1])) ##Representing a location closer to your endzone (0 + yardage)           32
    elif (row[1] == "Jets" and (row[7].split(" ")[0]) != "NYJ"):
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
    
