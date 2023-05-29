s1=input().lower().split()
s2=input().lower().split()
p=list(s1)
q=list(s2)
a=[]
for i in q:
    if i in p and i !=" ":
        a.append(i)
print(*a)