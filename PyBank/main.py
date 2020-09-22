#import dependencies
import os
import csv

#specify the file to write to
csvpath = os.path.join( "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Open the file using with 
with open(csvpath) as csvfile:

    # Initialize csv.reader
    csvreader= csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)

#count number of months
#list of months
from csv import DictReader

#makes all the dates in column into list, prints list, 
#set() finds uniqe values, and len() counts values
#used https://stackoverflow.com/questions/28283647/convert-csv-column-to-list
with open(csvpath) as f:
    a1 = [row['Date'] for row in DictReader(f)]
    #print(a1)
    Alyss = set(a1)
    lenny = len(Alyss)
    print ("Financial Analysis")
    print ("----------------------------")
    print ("Total Months: " + str(lenny))

#Profit and Loss / average change / increase max and min
with open(csvpath) as f:
    PatLeary = [row['Profit/Losses'] for row in DictReader(f)]
    #print(PatLeary)
    resPL = [int(i) for i in PatLeary]
    #print(resPL)
    SummaPL = sum(resPL)
    print('Total: ' + str(SummaPL))
    # USED https://stackoverflow.com/questions/2400840/finding-differences-between-elements-of-a-list
    Delta = [j-i for i, j in zip(resPL[:-1], resPL[1:])]
    #print(Delta)
    lenny2 = len(Delta)
    #print(lenny2)
    avgDelta = sum(Delta) / lenny2
    print('The average change is ' + str(avgDelta))
    print('Greatest Increase: ' + str(max(Delta)))
    print('Greatest Decrease: ' + str(min(Delta)))

#create a tx doc to save the output
import sys
sys.stdout = open('analysis.txt', 'w')
print( 'Financial Analysis' +
    " The number of months is " + str(lenny) + 
    ' The total P/L is ' + str(SummaPL) +
    'The average change is ' + str(avgDelta) +
    ' Greatest Increase in profits: ' + str(max(Delta)) +
    ' Greatest Decrease in profits: ' + str(min(Delta)))