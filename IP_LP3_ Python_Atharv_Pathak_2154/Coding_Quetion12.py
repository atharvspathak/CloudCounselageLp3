'''
Problem Statement:

Write a Python program to count the number of students of the individual class.

'''

from collections import Counter
m=int(input("Enter total number of tuples"))
t=[]
for i in range(m):
	a=[]
	classs=input()
	student=int(input())
	a.append(classs)
	a.append(student)
	t.append(tuple(a))

classes=t
students = Counter(class_name for class_name, no_students in classes)
print(students)

'''
Output:
Enter total number of tuples6                #Input total number of tuples
V                                            #Class
1                                            #Number of students 
VI                                           #Class
1                                            #Number of students
V                                            #Class
2                                            #Number of students
VI                                           #Class
2                                            #Number of students
VI                                           #Class
3                                            #Number of students
VII                                          #Class
1                                            #Number of students
Counter({'VI': 3, 'V': 2, 'VII': 1})         #Result
'''


