t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    i=0
    j=-1
    li=[]
    while i!=len(l) and j!=0 and j!=-(len(l)//2)-1:
          li.append(l[i])
          li.append(l[j])
          i=i+1
          j=j-1
    t=[]
#print(*li)
    t.append((l[len(l)//2]))
    if len(l)%2==0:
         print(*li)
    else:
         print(*((li)+t))
