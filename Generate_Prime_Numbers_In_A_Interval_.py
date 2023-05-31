import math
def isprime(n):
    s=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,s+1):
        if n%i==0:
            return False
    return n
t=int(input())
m=int(input())
l=[]
for i in range(t,m+1):
    l.append(i)
for i in l:
    if isprime(i):
        print(i)