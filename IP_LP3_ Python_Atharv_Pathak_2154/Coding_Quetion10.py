'''
Problem Statement:

Write a Python program to sort a list of elements using the selection sort algorithm.
Note: The selection sort improves on the bubble sort by making only one exchange for
every pass through the list.

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

'''
Output:
Total count of numbers 9                         #Input(n numbers)
14                                               #n number of input for sort
46
43
27
57
41
45
21
70
[14, 21, 27, 41, 43, 45, 46, 57, 70]            #Output(Sorted List)
'''


