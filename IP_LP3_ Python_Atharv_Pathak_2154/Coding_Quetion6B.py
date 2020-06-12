'''
Problem Statement:

Write a Python program to find the first appearance of the substring 'not' and 'poor' from
a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with
'good'. Return the resulting string.

'''

def removeNotpoor(ip:str)->str:
	findpoor = ip.find('poor')
	findnot= ip.find('not')

	if findpoor > findnot and findnot>0 and findpoor>0: #at least one poor one not and position of poor is after not
		ip = ip.replace(ip[findnot:(findpoor+4)], 'good')
		return ip
	else:
		return ip


ip1=input()
ip2=input()

print(removeNotpoor(ip1))
print(removeNotpoor(ip2))

'''
Output:
The lyrics is not that poor!                 #Input
The lyrics is poor!                          #Input
The lyrics is good!                          #Output
The lyrics is poor!                          #Output
'''


