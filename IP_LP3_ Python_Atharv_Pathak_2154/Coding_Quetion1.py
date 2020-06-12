'''
Problem Statement:

Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.

'''

a,b=map(int,input().split(" "))
print(a+b,"",a-b,"",a*b)

'''
Output:
3 2                       #Input
5  1  6                   #Output:Addition Substraction Multiplication
'''


