'''
Program:Check leap year or not

Input: Year as a input

Output: True or False
'''
def leap(year:int)->bool:
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    else:
        return False

year=int(input())
print(leap(year))

