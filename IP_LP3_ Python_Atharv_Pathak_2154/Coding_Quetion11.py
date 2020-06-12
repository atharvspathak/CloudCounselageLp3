'''
Problem Statement:

Write a Python program to get a week number.

'''

from datetime import date
y,m,d=map(int,input().split(","))  #Input in form of year,month,date
cdate = date(y,m,d)
week=list(cdate.isocalendar())
print(week[1])                    #Output total number of week

'''
Output:
2015,6,16           #Input
25                  #Output
'''


