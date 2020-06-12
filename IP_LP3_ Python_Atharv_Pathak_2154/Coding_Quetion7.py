'''
Problem Statement:

Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]

'''

celsius=int(input())
Fahrenheit=int(input())
degree=u"\N{DEGREE SIGN}"                #To get degree sign
print(celsius,degree+"C is",int((celsius*9/5)+(32)),"in Fahrenheit")
print(Fahrenheit,degree+"F is",(((5*Fahrenheit)-(160))//9),"in Celsius")

'''
Output:
60                               #Input
45                               #Input
60 °C is 140 in Fahrenheit       #Output
45 °F is 7 in Celsius            #Output
'''


