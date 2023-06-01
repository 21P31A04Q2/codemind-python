s=input()
l=list(s)
for i in range(0,len(l)):
    if l.count(l[i])==1:
        print(i)
        break
else:
    print("-1")