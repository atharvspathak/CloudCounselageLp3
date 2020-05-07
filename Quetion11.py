'''
Program:Number of week

Input: Year,Month,Date

Output:Number of week
'''

from datetime import date
y,m,d=map(int,input().split(","))  #Input in form of year,month,date
cdate = date(y,m,d)
week=list(cdate.isocalendar())
print(week[1])                    #Output total number of week
