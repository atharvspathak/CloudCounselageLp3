'''
Problem Statement:

Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0).

'''

def sum_series(n:int)->int:
	if n<=0:
		return 0
	else:
		return n+sum_series(n-2)


print(sum_series(int(input())))

'''
Sample Output 1:
6                   #Input
12                  #Output
Sample Output 2:
10                  #Input
30                  #Output
'''


