def nextprime(n):
    while True:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n
        n=n+1
def previouspime(n):
    while True:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n
        n=n-1
t=int(input())
for i in range(t):
    m=int(input())
    k=nextprime(m)
    h=previouspime(m)
    a=abs(m-k)
    b=abs(m-h)
    if a<b:
        print(k)
    else:
        print(h)
    