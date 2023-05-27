s1=input().lower()
s2=input().lower()
p=set(s1)
q=set(s2)
p.discard(" ")
q.discard(" ")
k=(p.symmetric_difference(q))
l=[]
for i in k:
    if i!=" " and i.isalpha():
        l.append(i)
l.sort()
print(''.join(l))