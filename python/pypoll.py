#import dependencies
import os
import csv
import pandas as pd

#read the csv file

path='election_data.csv'
file = pd.read_csv(path)


#number of voters 

Totalvoters=file["Voter ID"].count()

#find each candidate
Candidates = file.Candidate.unique()

# calculations 
Vote_Counts =file['Candidate'].value_counts()
Names = Vote_Counts.keys().tolist()
Votes = Vote_Counts.tolist()
Number_of_Names = len(Names)

#for loop to calculate the percentages
Percents =[]
for x in range(0,Number_of_Names):
	Percents.append(round(Votes[x]/Totalvoters *100 ,3))



#print statements
print('Election Results')
print('------------------------')
print('Total Votes :' + str (Totalvoters))
print('------------------------')
for x in range(0, Number_of_Names):
    print(str(Names[x]) + ': ' + str(Percents[x]) + '% (' + str(Votes[x]) + ')')
print('--------------------------')
print('Winner :' + Names[0])
print('---------------------------')


#writing file as .txt file
with open('Election_Resuts.txt', 'w+', newline = "\n") as ER:
    ER.write('Election Results\n')
    ER.write('-------------------------\n')
    ER.write('Total Votes: ' + str(Totalvoters)+ "\n")
    ER.write('-------------------------\n')
    for x in range(0, Number_of_Names):
        ER.write(str(Names[x]) + ': ' + str(Percents[x]) + '% (' + str(Votes[x]) + ')\n')
    ER.write('-------------------------\n')
    ER.write('Winner: ' + Names[0] + '\n')
    ER.write('-------------------------\n')
    


	
