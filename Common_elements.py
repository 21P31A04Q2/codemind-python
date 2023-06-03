n,m=map(int,input().split())
li=list(map(int,input().split()))
l=list(map(int,input().split()))
p=set(li)
q=set(l)
m=[]
t=p.intersection(q)
for i in li:
    if i in t:
        m.append(i)
for i in l:
    if i in t:
        m.append(i)
k=[]
for i in m:
    if i not in k:
        k.append(i)
print(*k)