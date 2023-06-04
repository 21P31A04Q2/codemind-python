t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    while n:
        r=n%10
        l.append(r)
        n=n//10
    l.sort()
    c=0
    for i in range(0,len(l)-1):
        if l[i]+1==l[i+1]:
            c+=1
    if len(l)==c+1:
        print("YES")
    else:
        print("NO")