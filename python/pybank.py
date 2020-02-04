#import libraries

import os
import pandas as pd 
import csv

#read csv file as df

ryan = pd.read_csv('budget_data.csv')

#renaming the columns 

ryan = ryan[['Date','Profit/Losses']]

#number of months variable

Months =ryan['Date'].count()

#net profits

Total_profits = ryan['Profit/Losses'].sum()

#empty array for change in profit
Profits = ryan['Profit/Losses']
Past_profit = Profits[0]
Change_in_profits =[]

#for loop to loop through data

for row in Profits:
	Change_in_profits.append(row - Past_profit)
	Past_profit = row


#new column for changes in profit
ryan["Change in Profit/Loss"]=Change_in_profits

#calculation of the average 

mean_change =sum(Change_in_profits) / len(Change_in_profits)

#calculation of maximum and minimum increases
Maxincrease =ryan['Change in Profit/Loss'].max()
Minincrease =ryan['Change in Profit/Loss'].min()

#use the loc function to locate date 
Indexedfile =ryan.set_index("Change in Profit/Loss")
MaxDate = Indexedfile.loc[Maxincrease ,"Date"]
MinDate = Indexedfile.loc[Minincrease ,"Date"]

#printing
print('Financial Analysis')
print('--------------------------------------')
print('Total Months:' + str (round(Months)))
print('Total:$' + str(round(Total_profits ,2)))
print('Average Change: $' + str(round(mean_change , 2)))
print('Greatest Increase in Profits:' + str(MaxDate) + '($' + str(Maxincrease)+')')
print('Greatest Decrease in Profits:' + str(MinDate) + '($' + str(Minincrease)+')')


#return results
with open('Bank_Results.txt', 'w+', newline = "\n") as r:
    r.write("Financial Analysis")
    r.write('----------------------------')
    r.write('Total Months:' +str (round(Months)))
    r.write('Total: $'+ str(round(Total_profits ,2)))
    r.write('Average Change:$ '+ str(round(mean_change , 2)))
    
    r.write('Greatest Increase in Profits:'+ str(MaxDate) + '($' + str(Maxincrease)+')')
    r.write('Greatest Decrease in Profits:'+ str(MinDate) + '($' + str(Minincrease)+')')

