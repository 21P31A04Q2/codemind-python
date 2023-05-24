r,c=map(int,input().split())
mat=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
p=[]
for i in mat:
    for j in i:
        s=0
    p.append(sum(i))
print(max(p))