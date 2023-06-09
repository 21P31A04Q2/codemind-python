def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
m=int(input())
p=m+reverse(m)
while p!=0:
    if reverse(p)==p:
        print(p)
        break
    else:
        p=reverse(p)+p