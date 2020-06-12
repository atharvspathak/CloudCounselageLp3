'''
Problem Statement:

Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the
column starting with index 0.
The matrix will hold distinct integers as elements.
We need to find a distinct number of positional elements which are either the minimum
or maximum in their corresponding row or column.
Please return -1 if any row or any column has multiple minimum or maximum
elements.

'''
def findminmax(matrix):
	nrs=len(matrix)
	cnt=0
 
	for row in matrix:
		for indexCol, element in enumerate(row):
			if element==min(row) or element==max(row):
				if row.count(element)>1:
					return -1
				cnt=cnt+1
 
			else:
				listColumn=[]
 
				for indexRow in range(0,nrs):
					listColumn.append(matrix[indexRow][indexCol])
 
					if element==min(listColumn) or element==max(listColumn):
						if listColumn.count(element)>1:
							return -1
						cnt=cnt+1
	return cnt

m = int(input()) 
n = int(input())  
matrix = [] 

for i in range(m):		  
	r =[] 
	for j in range(n):	  
		r.append(int(input())) 
	matrix.append(r) 
print(findminmax(matrix)) 

'''
Output:
3            #value of m
3            #value of n
1            #element in matrix [0][0]
3            #element in matrix [0][1]
4            #element in matrix [0][2]
5            #element in matrix [1][0]
2            #element in matrix [1][1]
9            #element in matrix [1][2]
8            #element in matrix [2][0]
7            #element in matrix [2][1]
6            #element in matrix [2][2]
10           #Result
'''



