# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:24:57 2026

@author: ISHIKA TOMAR
"""
1
'''
salary=int(input("enter the salary"))
year=int(input("enter the year of sevice"))
bonus=(5/100)*salary
if year>5:
    print("bonus",bonus)
else:
    print("no bonus")
'''
2
'''
passward=input()
if passward==("s3cr3t!p@ssword"):
    print("welcome")
else:
    print("wrong passward")
 '''
3 
''' 
shape=float(input())
side=float(input())
if shape=="square":
    area=side*side

elif shape=="rectangle":
    length=float(input())
    width=float(input())
    area=length*width
    
elif shape=="circle":
    radius=float(input())
    area=3.14*radius*radius

elif shape=="triangle":
    base=float(input())
    height=float(input())
    area=0.5*base*height
    
    print(area) 
'''
4
'''
hours=int(input("enter hour"))
minutes=int(input("enter minutes"))
minutes=minutes+15
if minutes>=60:
    minutes=minutes-60
    hours=hours+1
if hours==24:
    hours=0
print(f"{ hours}:{minutes}")
'''
5
'''
distance=float(input("enter distance:"))
time=int(input("Enter day or night:"))
if time=="day":
    taxi=33.58+distance*37.89
else:
    taxi=33.58+distance*43.17
    
    if distance>=100:
        train=distance*2.88
        print(train)
    elif distance>=20:
        bus=distance*4.32
        print(bus)
    else:
        print(taxi)
'''
6
'''
holidays=int(input("enter the holiday"))
workdays=365-holidays
games=workdays*63+holidays*127
if games<30000:
   print("Tom sleep well")
else:
    print("Tom not sleep well")
 '''
7
'''
budget=float(input("enter budget"))
season=int(input("enter season"))
if budget<=100:
    place="bulgaria"
    if season=="summer":
        spent=budget*0.40
    else:
        spent=budget*0.70
elif budget<=1000:
    place="balkans"
    if season=="summer":
        spent=budget*0.40
    else:
        spent=budget*0.80
else:
        place="europe"
        spent=budget*0.90
        
        print(place)
        print(spent)
'''
8
'''
for i in range(1,1001):
   if i %10==6:
    print(i) 
'''
9
'''
n=int(input())
total=0

for i in range(n):
    num=int(input())
    total=total+num
    
print(total)
'''
10
'''
n=int(input("enter a number"))
for i in range(1,21):
    print(n,"x",i,"=",n*i)
'''
11
'''
x=int(input())
y=int(input())
n=int(input())

count=0

for i in range(x,y+1):
    if i%n!=0:
        print(i,end=" ")
        count+=1
print()
print(count)
'''
12
'''
n=int(input("enter n"))
product=1
while n>0:
    digit=n%10
    product=product*digit
    n=n//10
    print(product)
 '''
13
'''
n=int(input())
large=0
small=0
while True:
    bill=int(input())
    if bill==-999:
        break
    if bill>n:
        large+=1
    else:
        small+=1
        print(large)
        print(small)
'''
4
'''
n=int(input())
p=int(input())
if n<=0 or p<0:
    print("invalid")
else:
    result=1
    count=0
while count<p:
    result=result*n
    count+=1
print(result)
'''


n=int(input())
m=int(input())
original=m
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10    
if reverse==m:
    print("Yes")
else:
    print("No") 



        

                 
        
    
    
     
        
        
    
    
     

    
