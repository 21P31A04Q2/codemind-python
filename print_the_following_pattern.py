m=int(input())
l=[]
for i in range(1,m+1):
    l.append(i)
s = [str(integer) for integer in l]
a_string = "".join(s)
n = int(a_string)
p=str(n)
q=len(p)
#(q)
while n:
    r=n%10**q
    print(r)
    n=n//10
    
