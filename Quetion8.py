'''
Program:Sum of series of n+(n-2)+(n-4)

Input: Number for which sum has to calculate

Output: Sumation of number
'''
def sum_series(n:int)->int:
	if n<=0:
		return 0
	else:
		return n+sum_series(n-2)


print(sum_series(int(input())))

