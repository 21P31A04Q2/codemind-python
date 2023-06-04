def rotate(l,m):
    for i in range(m):
        l.insert(0,l.pop())
    return l
t=int(input())
for i in range(t):
    n,h=map(int,input().split())
    li=list(map(int,input().split()))
    print(*(rotate(li,h)))