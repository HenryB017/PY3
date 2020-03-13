# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:46:27 2020

@author: hboateng
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


### Import excel file from H: drive 
excel_file = 'nba.xlsx'
nba = pd.read_excel(excel_file)

#DATA MANIPULATION

### Single Column
salary= nba['Salary']
PN= nba['Name']
'''
print (salary)
'''

#Head and Tail

'''
print (nba.head())
print (nba.tail())
'''

### Selecting columns (Salary and Age)
salary_age = nba[['Salary', 'Age']]
###Using the loc function
salary_age2= nba.loc[:, ['Salary', 'Age']]

'''
print (salary_age2)
'''

### Using iloc function 
player_points = nba.iloc[:,[0,3]]
player_points2 = nba.iloc[:, 0:4]

### Filtering through data
### Players who average more than 22ppg

player_ppg = nba[nba.PPG >= 22]

'''
print (player_ppg)
'''

### Players who earned more than 32000000
player_salary = nba[nba.Salary >= 32000000]

'''
print (player_salary)
'''

### Players that average more than 20 and earn more than 26000000
playerPPG_salary = nba[(nba.Salary > 26000000) & (nba.PPG > 26)]
### Players that average less then 25PPG and earn more than using ~
playerPPG_salary2 = nba[~(nba.Salary > 26000000) & ~(nba.PPG > 25)]

'''
print (playerPPG_salary)
'''

#Statistics on Salary: Measures of Central Tendencies 
#Mean #List of elements 
salary= nba['Salary']
l_salary = len(salary)
sum_salary = sum(salary)
mean = sum_salary / l_salary 

'''
print (mean)
'''

'''
#This is another way to compute mean through looping but I couldn't debug/complete.
#Learnt this method on codecademy 
def mean(salary):
    total = 0 
    for num in salary:
        total = total + num
    return total/ len(salary)
'''
'''
print(mean [salary]) ## For loop
'''

#Median 
#No need to sort salary becasue its already in ascending order 

if l_salary % 2 == 0:
    median1 = salary [l_salary//2]
    median2 = salary [l_salary//2-1]
    median = (median1 + median2)/ 2
else:
    median = salary [l_salary//2]

'''
print (median)
'''

#Mode #Using the Scipy Library 
mode= stats.mode(salary)
'''
print (mode)
'''
'''
### DATA VISUALISATION
#Bar chart showing player and their salary 
salary= nba['Salary']
PN= nba['Name']

plt.bar(PN, salary)
plt.title('Player Salary Chart in USD')
plt.xlabel('Player Name')
plt.ylabel('Salary in millions ($)')
plt.show()
'''
#Line graph showing Salary and Age
salary = nba['Salary']
PA= nba.Age
PA.sort()
print(PA)

'''
plt.plot(PA, salary)
plt.title('Salary plot against Player Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
'''