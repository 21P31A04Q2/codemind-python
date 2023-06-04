n=int(input())
li=list(map(int,input().split()))
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[]
for i in d:
    if d[i]!=1:
        l.append(d[i])
l1=[]
for i in l:
    l1.append(i//2)
print(sum(l1))