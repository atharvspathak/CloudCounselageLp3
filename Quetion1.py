'''
Program:Addtion Substraction Mutiplication

Input:Two numbers

Output:Addition Substraction Multiplication of given two numbers
'''
a,b=map(int,input().split(" "))

if  a>=0 and a<=pow(10,10) and b>=0 and b<=pow(10,10):
	print(a+b,"",a-b,"",a*b)
else:
	print("Invalid input")
