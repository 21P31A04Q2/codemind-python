n=int(input())
temp=n
var=n
org=n
c=0
n1=0
n2=1
l=[]
while c<=n:
    n3=n1+n2
    c=c+1
    l.append(n3)
    n1=n2
    n2=n3
while True:
    temp=temp+1
    if temp in l:
        p=temp
        break
while True:
    var=var-1
    if var in l:
        q=var
        break
a=abs(org-p)
b=abs(org-q)
if a<b:
    print(p)
if b<a:
    print(q)
if a==b:
    print(q,p)