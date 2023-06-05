n=int(input())
lst=list(map(int,input().split()))
l=[]
d={}
for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(i,d[i],end=" ")