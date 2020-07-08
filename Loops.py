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
