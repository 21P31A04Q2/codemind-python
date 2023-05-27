def sort(s):
    l=list(s)
    h=[]
    for i in s:
        if i.isalnum():
            pass
        else:
            h.append(i)
#print(h)
    for i in range(0,len(l)):
         for j in range(0,len(h)):
                if l[i]==h[j]:
                    l[i]="*"            
    k=[]
    for i in range(0,len(l)):
         if l[i]!="*":
            k.append(l[i])
    k.sort()
    i=0
    j=0
    while i!=len(l) and j!=len(k):
        if l[i]!="*":
            l[i]=k[j]
            j=j+1
        i=i+1
    i=0
    j=0
    while i!=len(l) and j!=len(h):
        if l[i]=="*":
            l[i]=h[j]
            j=j+1
        i=i+1
    return(''.join(l))
n=input()
x=n.split()
for i in x:
    print(sort(i),end=" ")
