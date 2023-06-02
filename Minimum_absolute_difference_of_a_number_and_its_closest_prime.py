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
m=int(input())
a=abs(m-nextprime(m))#4
b=abs(m-previouspime(m))#2
l=[]
l.append(a)
l.append(b)
print(min(l))