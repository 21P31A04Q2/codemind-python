def length(n):
    l=list(n)
    p="aeiouAEIOU"
    c=0
    if l[0] in p and l[-1] not in p:
        c=c+1
    return c
s=input().split()
k=list(s)
l1=[]
for i in k:
   l1.append(length(i))
print(sum(l1))