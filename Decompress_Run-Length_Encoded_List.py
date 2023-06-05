def repeat(f,n):
    l=[]
    for i in range(f):
        l.append(n)
    return l
n=int(input())
k=[]
li=list(map(int,input().split()))
for i in range(0,len(li)-1):
    t=repeat(li[i],li[i+1])
    k.append(t)
for i in range(0,len(k),2):
    print(*k[i],end=" ")