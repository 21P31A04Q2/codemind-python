s=input()
l=[]
for i in s:
    if i!=" ":
        l.append(i)
q=max(l)
h=min(l)
m=[]
print(h,l.count(h),q,l.count(q),end=" ")