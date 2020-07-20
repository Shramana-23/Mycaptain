"""Fibonacci series"""
i=0
j=1
n=int(input("Enter the number of terms"))
c=0
while c<n:
    print(i)
    x=i+j
    i=j
    j=x
    c+=1

    
    
"""POSITIVE NUMBERS IN LIST"""
lst=[]
n=int(input("Enter the number of elements"))
for i in range(0,n):
    x=int(input())
    lst.append(x)
for j in lst:
    if j>0:
        print(j)
