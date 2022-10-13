def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def swap(l,i,j):
    l[i],l[j]=l[j],l[i]

def max_pos(l,n,i):
    if left(i)>=n:
        return i
    k=i
    if l[k]<l[left(i)]:
        k = left(i)
    if right(i)<n and l[k]<l[right(i)]:
        k = right(i)
    return k

def heapify_up(l,i):
    p = parent(i)
    e = l[i]
    while p>=0 and l[p]<e:
        l[i]=l[p]
        i = p
        p = parent(i)
    l[i]=e

def heapify_down(l,n,i):
    m = max_pos(l,n,i)
    while m!=i:
        swap(l,m,i)
        i = m
        m = max_pos(l,n,i)

def build_heap(l):
    for i in range(len(l)):
        heapify_up(l,i)

def k_largest_element(l,k):
    build_heap(l)
    for i in range(k):
        largest_element = extract_max(l)
    return largest_element 

def extract_max(l):
    m = l[0]
    n = len(l)-1
    swap(l,0,n)
    l[:]=l[:n]
    heapify_down(l,n,0)
    return m
        
l = [3,4,1,9,2,5]
k = 4
print(k_largest_element(l,k))

