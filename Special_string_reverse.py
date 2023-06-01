s=input()
l=list(s)
p=[]
k=[]
for i in range(0,len(l)):
    if not l[i].isalpha():
        k.append(l[i])
for i in range(0,len(l)):
    if l[i].isalpha():
        p.append(l[i])
    else:
        l[i]="*"
i=0
j=0
p.reverse()
while i!=len(l) and j!=len(p):
    if l[i]!="*":
        l[i]=p[j]
        j=j+1
    i=i+1
i=0
j=0
while i!=len(l) and j!=len(k):
    if l[i]=="*":
        l[i]=k[j]
        j=j+1
    i=i+1
print(''.join(l))