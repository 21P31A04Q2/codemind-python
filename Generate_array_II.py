def repeat(p,n):
    l=[]
    for i in range(p):
        l.append(n)
    return l
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(0,len(l)-1):
    t=(repeat(l[i+1],l[i]))
    m.append(t)
li=[]
for i in range(0,len(m),2):
    li.append(m[i])
for i in li:
    for j in i:
        print(j,end=" ")
