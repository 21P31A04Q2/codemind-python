N=int(input())
li=list(map(int,input().split()))
odd=[odd for odd in li if odd%2!=0]
print(sum(odd))