'''
Input: 
Size of matrix m*n
Enter the values in matrix(m*n)
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

