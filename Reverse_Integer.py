n=int(input())
rev=0
temp=n
n=abs(n)
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp>0:
    print(rev)
else:
    print('-%d'%rev)