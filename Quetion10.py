'''
Program:Selection Sort

Input:
Enter The Total count of numbers
Enter the numbers

Output:Sorted list
'''
def selectionSort(a):
	for i in range(len(a)):
		minpos=i
		for j in range(i+1,len(a)):
			if a[j]<a[minpos]:
				minpos=j
		if minpos!=i:
			a[i],a[minpos]=a[minpos],a[i]
	return a



n=int(input("Total count of numbers "))
a=[]
for i in range(n):
	a.append(int(input()))

print(selectionSort(a))


