'''
Program:Count number of student from individual class
Sample Input:
Enter total number of tuples6
v
1
vi
1
v
2
vi
2
vi
3
vii
1

sample output:
Counter({'vi': 3, 'v': 2, 'vii': 1})

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
