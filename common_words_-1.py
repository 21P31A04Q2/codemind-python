s1=input().lower().split()
s2=input().lower().split()
k=set(s1)
p=set(s2)
k.discard(" ")
p.discard(" ")
t=(k.intersection(p))
c=0
for i in t:
    c+=1
print(c)