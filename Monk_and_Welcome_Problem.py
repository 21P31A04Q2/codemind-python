n=int(input())
li=list(map(int,input().split()))
l=list(map(int,input().split()))
i=0
j=0
s=[]
while i!=len(li) and j!=len(l):
    s.append(li[i]+l[j])
    i=i+1
    j=j+1
print(*s)