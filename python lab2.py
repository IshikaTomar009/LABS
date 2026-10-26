# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:27:57 2026

@author: ISHIKA TOMAR
"""
1
'''
x=int(input("Enter the number"))
if x%5==0:
    print("Hii")
else:
    print("Bye")
'''
2
'''
X=int(input("Enter the length1"))
Y=int(input("Enter the Length2"))
H=int(input("Enter the Height"))
area=0.5*(X+Y)*H
print("Area of trapazoid",area)
'''
3
'''
weight=int(input("Enter the weight"))
height=int(input("Enter the height"))
bmi=weight/(height*2)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("slightly overweight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")
'''
4
'''
ch=input("Enter the character")
if ch=="a"or ch=="e"or ch=="i" or ch=="o" or ch=="u" :
    print("Vowels")
else:
    print("Consonant")
'''
5
'''
growth=float(input("enter the growth"))
x=2.19*10**14
y=4.68*10**14
percentage=((y-x)/x)*100
print("percentage of bacterial growth",percentage)
'''
6
'''
month=int(input("Enter the month"))
years=month//12
month=month%12
print("years",years)
print("month",month)
'''
7
'''
color=input("Enter the color:")
mode=input("Enter the mode:")
if color=="Blue" and mode=="flashing":
   print("forcast:clouds view")
elif color=="Blue"and mode=="steady":
   print("forcast:clear view")
elif color=="Red"and mode=="steady":
   print("forcast:rain ahead")
elif color=="Red"and mode=="flashing":
   print("forcast:snow instead")
else:
    print("weather forcast")
'''
8
'''
coast=int(input("Enter the coast"))
revenue=int(input("Enter the revenue"))
if coast==revenue:
    print("Break even")
else:
    print("profit or loss")
'''
9
'''
widgets=int(input("Enter the number of widgets"))
if widgets>=100:
    total=widgets*20
else:
    total=widgets*25
print("Total cost",total)
'''
10
'''
pounds=float(input("Enter the number of pounds"))
cash=float(input("Enter the cash tendered"))
cost=pounds*2.50
if cash>=cost:
   change=cash-cost
   print("change",change)
else:
   owed=cost-cash
   print("Owed",owed)
'''
11
'''
a=int(input("Enter the number1"))
b=int(input("Enter the number2"))
c=int(input("Enter the number3"))
if a>b:
    if a>c:
     print("a is largest")
else:
     print("c is largest")
if b>c:
     print("b is largest")
else:
     print("c is largest")
'''
12
'''
basic_salary=float(input("enter the salary")) 
HRA=0.20*basic_salary
TA=0.05*basic_salary
DA=0.10*basic_salary
cross_salary=basic_salary+HRA+TA+DA
print("HRA",HRA)
print("TA",TA)
print("DA",DA)
print("cross_salary",cross_salary)
'''
13
'''
basic_salary=float(input("Enter the salary"))
HRA=0.20*basic_salary
TA=0.05*basic_salary
DA=0.10*basic_salary
cross_salary=basic_salary+HRA+TA+DA
if basic_salary<300000:
    print("Income tax is 0%")
elif basic_salary<1000000:
    print("Income tax is 10%")
elif basic_salary<2500000:
    print("Income tax is 20%")
else:
    print("Income tax is 30%")
    print("HRA",HRA)
    print("TA",TA)
    print("DA",DA)
    print("cross_salary",cross_salary)
'''
14
'''
income=float(input("enter the income"))
if income<=20000:
    tax=0.02*income
elif income<=50000:
    tax=400+0.025*(income-20000)
else:
    tax=1150+0.035*(income-50000)
    print("Tax",tax)
'''
1
'''
X1=float(input("Enter the X1"))
Y1=float(input("Enter the Y1"))
X2=float(input("Enter the X2"))
Y2=float(input("Enter the Y2"))
r=float(input("Enter the radius of the circle"))
d=((X2-X1)**2+(Y2-Y1)**2)
if d<r:
    print("point lies inside")
elif d==r:
    print("point lies on the boundary")
else:
    print("point lies outside")
'''
2
'''
s=int(input("Enter the side of regular pentagon"))
area=(5*s**2)/(4*0.726)
print("Area of regular pentagon",area)
'''
3
'''
a=int(input("Enter the first angle"))
b=int(input("Enter the second angle"))
c=int(input("Enter the third angle"))
if a+b+c<=180:
    print(" form a triangle:")
elif b>90:
    print("acute angled triangle")
elif b<90:
    print("obtuse angled triangle")
else:
    print("right angled triangle")
'''
4
'''
a=int(input("enter the number1"))
b=int(input("enter the number2"))
c=int(input("enter the number2"))
d=int(input("enter the number4"))
sum1=a+b
sum2=c+d
if sum1==sum2:
    print("equal")
else:
    print("not equal")
'''
5
'''
n=int(input("enter a 5digit number"))
d1=n//10000
d2=(n//1000)%10
d3=(n//100)%10
d4=(n//10)%10
d5=n%10
if d1>=d2 and d1>=d3 and d1>=d4 and d1>=d5:
    print("largest d1")
elif d2>=d3 and d2>=d4 and d3>=d5:
    print("Largest d2")
elif d3>=d4 and d3>=d5:
    print("Largest d3")
elif d4>=d5:
    print("largest d4")
else:
    print("Largest d5")
'''
6
'''
a=int(input("enter the integer1"))
b=int(input("enter the integer2"))
c=int(input("enter the integer3"))
a=a+b+c
a=a-b-c
a=a-b-c
a=a-b-c
print("rotation")
print("a",a)
print("b",b)
print("c",c)
'''
7
'''
n=int(input("enter the 3-digit number1"))
a=n//100
b=(n//10)%10
c=n%10
sum=a+b+c
if n%sum==0:
    print("harshad number")
else:
    print("not harshad number")
    '''
8
'''
V=int(input("enter the quantity of water"))
N=int(input("enter the number of days"))
water=v**(0.95**n)+200*(1-0.95**n)
if v<0:
    print("invalid input")
else:
     print("Quantity of water=",water)
'''
9
'''
a1=int(input("enter a1"))
b1=int(input("enter b1"))
c1=int(input("enter c1"))
a2=int(input("enter c2"))
b2=int(input("enter b2"))
c2=int(input("enter c2"))
x=-b1/a1
y=-a2/b2
if a1==-a2:
    print("y")
else:
    print("parallel lines")
'''




    
    
    








    

                
    
    
    

    

    


    





    

    
