## taking input from user
r,c=map(int,input().split())
mat=[]# creating an empty list to store matrix rows
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
p=[]
for i in mat:
    p.append(sum(i))
print(sum(p))