'''
Problem Statement:

You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.

'''

n=int(input())
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

'''
Output:
4                      #Input
bcdef                  #Input
abcdefg                #Input
bcde                   #Input
bcdef                  #Input
3                      #Output Distinct word Counr
2 1 1                  #Number of times repeated
'''


