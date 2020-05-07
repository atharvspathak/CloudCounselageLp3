'''
Program:Remove duplicates charecters from string

Input:String

Output:String without duplicate charecters
'''
x=input()
li=[0]*122
y=''
for i in x:
	ascii = ord(i)
	if li[ascii]==0:
		li[ascii]=1
		y=y+i
 
print(y) 

	
