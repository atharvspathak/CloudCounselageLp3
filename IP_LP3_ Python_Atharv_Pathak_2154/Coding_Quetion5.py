'''
Problem Statement:

You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.

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

'''
Sample Output 1:
ababacd                       #Input
abcd                          #Output
Sample Output 2:
AaaCccBbbB                    #Input
AaCcBb                        #Output
'''


