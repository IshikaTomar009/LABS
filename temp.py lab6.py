# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:13:28 2026

@author: ISHIKA TOMAR
"""
2
'''
n=int(input("enter the number"))
i=0
while i<=1000:
    if i%n==0 and i%4!=0:
        print(i,end=" ")
    i+=1
    continue 
'''
31
'''
n=int(input("enter the number"))
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    '''
32
'''
n=int(input("enter the number"))
i=n
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=1
'''
33
'''
n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''
4
'''
n=int(input("enter a positive integer"))
octal=""

while n>0:
    remainder=n%8
    octal=str(remainder)+octal
    n=n//8
    
print("octal=",octal)
'''
5
'''
n=int(input())
distance=[]
for i in range(n):
    distance=int(input())
    distance.append(distance)
    
largest=distance[0]
second=none

for distance in distance:
    if distance>largest:
        second=largest
        largest=distance
elif distance>second and distance<largest:
    
            second =distance
            
        print(largest)
        print(second)
'''
6
'''
a=int(input())
num=1
while num<=a:
    n=num
    n=len(str(num))
    total=0
    while n>0:
        digit=n%10
        total+=digit**digit
        n=n//10
        
    if total==num:
     print(num,end="")
     num+=1 
'''
7
'''
n=int(input("enter n:"))
i=1
print()
'''
8
'''
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print() 
'''
9
'''
n=int(input("enter n"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num=num+1
    print()
'''
10
'''
n=int(input("enter n:"))
for i in range( 1, n + 1):
    print(" " * (n - i),end="")
    for j in range(2 * i - 1):
        print("*",end=" ")
    print()
for i in range(n - 1, 0 , -1):
    print(" " * (n - i),end="")
    for j in range(2 * i - 1):
        print("*",end=" ")
    print()
'''
    
    