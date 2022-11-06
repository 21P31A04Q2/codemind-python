N=int(input())
li=list(map(int,input().split()))
p=sum(li)
q=len(li)
r=p//q
if r in li:
    print("True")
else:
    print("False")