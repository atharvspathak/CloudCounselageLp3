'''
Proram: Calculate number of common divisors

Input: Two numbers

Output:Count of common divisors
'''
def gcd(a, b):                                          #calculate greatest common divisor to improve efficincy

	if (a == 0): 
		return b; 

	return gcd(b%a, a)

a = int(input())
b = int(input())

cnt = 0
for i in range(1, gcd(a, b)+1):
	if a%i==0 and b%i==0:
		cnt=cnt+1
print(cnt)

