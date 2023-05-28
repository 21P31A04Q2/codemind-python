def length(l):
    i=0
    j=-1
    m=[]
    while i!=len(l) and j!=0 and j!= -(len(l)//2)-1:
        m.append(l[i])
        m.append(l[j])
        i=i+1
        j=j-1
    i=0
    j=1
    h=[]
    while i!=len(m) and j!=len(m)-2 :
        if  ((m[i] not in "aeiou" ) and (m[j] in "aeiou")) or ((m[i] in "aeiou") and (m[j] not in "aeiou")):
            h.append(m[i])
            h.append(m[j])
        i=i+2
        j=j+2 
    return len(h)//2
k=input().split()
p=list(k)
n=[]
for i in p:
    n.append(length(i))
print(sum(n))