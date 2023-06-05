def small(k,li):
    c=0
    n=k
    for i in range(0,len(li)):
            if n>li[i]:
                c=c+1
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(small(i,l),end=" ")