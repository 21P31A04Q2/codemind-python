n=int(input())
li=list(map(int,input().split()))
k=int(input())
l=[]
for i in range(0,len(li)):
    if k==li[i]:
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print("-1")