def sort(s):
    l=list(s)
    i=0
    for i in range(0,len(l)):
        if l[i] not in "aeiouAEIOU":
            l[i]="*"
    m=[]
    for i in s:
        if i not in "aeiouAEIOU":
            m.append(i)
    m.sort()
    q=list(m)
    i=0
    j=0
    while i!=len(l) and j!=len(q):
        if l[i]=="*":# 
            l[i]=q[j]
            j=j+1
        i=i+1
    return (''.join(l))
n=input()
x=n.split()
l=[]
p=list(n)
for i in x:
    l.append(sort(i))
print(*l)