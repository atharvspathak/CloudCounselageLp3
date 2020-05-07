'''
Input:
'The lyrics is not that poor!'
'The lyrics is poor!'

Sample Output:
'The lyrics is good!'
'The lyrics is poor!'
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

