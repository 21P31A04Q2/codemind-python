s=input()
l=list(s)
q="aeiouAEIOU"
k=[]
for i in range(0,len(l)):
    if l[i] in q:
        k.append(l[i])
for i in range(0,len(l)):
    if l[i] in q:
        l[i]="*"
#print(l)
k.reverse()
i=0
j=0
while i!=len(l) and j!=len(k):
    if l[i]=="*":
        l[i]=k[j]
        j=j+1
    i=i+1
print(''.join(l))
        