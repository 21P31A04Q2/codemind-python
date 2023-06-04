n=int(input())
li=list(map(int,input().split()))
for i in range(1,len(li)):
    if li[i]!=0:
        li[i]=li[i]+li[i-1]
print(max(li))