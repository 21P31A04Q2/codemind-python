import math
n=int(input())
li=list(map(int,input().split()))
print(math.gcd(*li))