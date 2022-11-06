N=int(input())
li=list(map(int,input().split()))
p=sum(li)
q=len(li)
r=p//q
ct=0
for i in li:
   if i>=r:
      ct=ct+1
   else:
       pass
print(ct)