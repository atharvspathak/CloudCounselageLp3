'''
Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1
'''
n=int(input())

if n>=1 and n<=pow(10,5):
	c=[]                              #To store input words
	rem=[]							  #save key to prevent it from unwanted iteration

	for i in range(n):
		c.insert(0,input())
	c=c[::-1]                         #To get sequetial input in list

	print(len(set(c))) 				  #set does not contain duplicate elements.so print length of set

	for i in range(len(c)):
		cnt=0
		key=c[i]
		if key not in (rem):
			for j in range(i,len(c)):
				if key==c[j]:
					cnt=cnt+1
					
			rem.insert(0,key)
			print(cnt,end=" ")
else:
	print("Invalid Input")
			
	

