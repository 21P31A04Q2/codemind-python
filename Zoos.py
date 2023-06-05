s=input()
c=0
k=0
for i in s:
    if i=="z":
        c+=1
    else:
        k+=1
if (2*c)==k:
    print("Yes")
else:
    print("No")