def most_frequent(s):
    d=dict()
    for x in s:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    return d
output=most_frequent(st)
st=input("Enter the string")
l=list(output.values())

l.sort()
print(l)
for i in l:
    print(output[i],i)
