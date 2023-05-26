def count(n):
    p=max(n)
    return ord(p)
def counts(n):
    g=min(n)
    return ord(g)
s=input().split()
l=list(s)
k=[]
for i in l:
    k.append(count(i))
    k.append(counts(i))
s=0
d=0
for i in range(0,len(k)):
    if i%2==0:
        s+=k[i]
    else:
        d+=k[i]
print(s-d)