n=int(input())
li=list(map(int,input().split()))
if n%2!=0:
    li.append(0)
print(*li)