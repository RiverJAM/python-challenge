#import dependencies
import os
import csv
from csv import DictReader

#specify the file to write to
csvpath = os.path.join( "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#define variables
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Tooley_votes = 0
# Open the file using 
with open(csvpath) as csvfile:

    # Initialize csv.reader
    csvreader= csv.reader(csvfile, delimiter=',')

    print(csvreader)
 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") don't need to print this
    print('Election Results')
    print('----------------------')




   
with open(csvpath) as f:
    a1 = [row['Voter ID'] for row in DictReader(f)]
    #print(a1)
    Alyss = set(a1)
    Total_Votes = len(Alyss)
    print("Total number votes:  " + str(Total_Votes))
    print('------------------------')

#with open(csvpath) as f:
    #a2 = [row['Candidate'] for row in DictReader(f)]
    
    #from collections import Counter 
    #res = dict(Counter(a2)) 

    #printing result  
    #print("The elements frequency : " + str(res))
    

    #loop to count votes for each
with open(csvpath) as csvfile:

    # Initialize csv.reader
    csvreader= csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #a2 = [row['Candidate'] for row in DictReader(f)]
        
        if str(row[2]) == 'Khan':
            Khan_votes = Khan_votes +1 
        elif str(row[2]) == "O'Tooley":
            Tooley_votes = Tooley_votes + 1
        elif str(row[2]) == "Li":
            Li_votes = Li_votes + 1
        elif str(row[2]) == "Correy":
            Correy_votes = Correy_votes + 1
    
    Khan_percentage = int((Khan_votes /Total_Votes) *100)
    Li_percentage = int((Li_votes /Total_Votes)*100)
    Correy_percentage = int((Correy_votes /Total_Votes)*100)
    Tooley_percentage = int((Tooley_votes /Total_Votes)*100)

    #Finding a winner
    if Khan_percentage > Li_percentage & Correy_percentage & Tooley_percentage:
        Winning_C = "Khan"
    elif Li_percentage > Khan_percentage & Correy_percentage & Tooley_percentage:
        Winning_C = "Li"
    elif Correy_percentage > Khan_percentage & Li_percentage & Tooley_percentage:
        Winning_C = "Correy"
    elif Tooley_percentage> Khan_percentage & Li_percentage & Correy_percentage:
        Winning_C = "O'Tooley"


    print('Khan ' + str(Khan_percentage) +'% ' + '(' + str(Khan_votes) + ')')
    print('Correy ' + str(Correy_percentage) +'% ' + '(' + str(Correy_votes) + ')')
    print('Li ' + str(Li_percentage) +'% ' + '(' + str(Li_votes) + ')')
    print("O'Tooley " + str(Tooley_percentage) +'% ' + '(' + str(Tooley_votes) + ')')

    print('------------------')
    print('Winner: ' + str(Winning_C))
    print('-------------------')

    import sys
sys.stdout = open('analysisPoll.txt', 'w')
print('Election Results' + '----------------------' + "Total number votes:  " + str(Total_Votes) + '------------------------' + 'Khan ' + str(Khan_percentage) + '% ' + '(' + str(Khan_votes) + ')' + 'Correy ' + str(Correy_percentage) + '% ' + '(' + str(Correy_votes) + ')' +
'Li ' + str(Li_percentage) + '% ' + '(' + str(Li_votes) + ')' +
"O'Tooley " + str(Tooley_percentage) +'% ' + '(' + str(Tooley_votes) + ')' +
'------------------' +
'Winner: ' + str(Winning_C) +
'-------------------')