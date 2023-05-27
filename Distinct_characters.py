s=input().lower()
l=[]
for i in s:
    if i!=" " and s.count(i)==1:
        l.append(i)
l.sort()
print(''.join(l))