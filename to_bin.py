def to_01list(n):
    l = []
    while n!=0:
        l.append(n%2)
        n=n//2
    return l

def bin_inc_mut(n):
    i = 0
    while i<len(n) and n[i]==1:
        n[i]=0
        i=i+1
    if i==len(n):
        n.append(1)
    else:
        n[i]=1

def bin_inc(l):
    i=0
    r=l.copy()
    while i<len(n) and r[i]==1:
        n[i]=1
        i=i+1
    if i==len(n):
    


l = to_01list(6)
print(l)
