n=int(input())
li=list(map(int,input().split()))
a={}
for i in li:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1
for i in a:
    if a[i]!=1:
        print(i)
        break