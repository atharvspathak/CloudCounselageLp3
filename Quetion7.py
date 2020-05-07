'''
Program:Conversion (1)Celsius to Fahrenheit
				   (2)Fahrenheit to Celsius
Input: Temprature in Celsius
	   Temprature in Fahrenheit

(Sample)Output: 
60 °C is 140 in Fahrenheit
45 °F is 7 in Celsius

'''
celsius=int(input())
Fahrenheit=int(input())
degree=u"\N{DEGREE SIGN}"                #To get degree sign
print(celsius,degree+"C is",int((celsius*9/5)+(32)),"in Fahrenheit")
print(Fahrenheit,degree+"F is",(((5*Fahrenheit)-(160))//9),"in Celsius")
