def max_heap():
    return []

def is_empty(h):
    return h==[]

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def add(v,l):
    l.append(v)
    heapify_up(l,len(l)-1)
        
def heapify_up(l,i):
    p = parent(i)
    e = l[i]
    while p>=0 and l[p]<e:
        l[i]=l[p]
        i = p
        p = parent(i)
    l[i]=e

def heapify_down(heap,start):
    heap[start]=heap[len(heap)-1]
    heap[:] = heap[:len(heap)-1]
    i = start
    e = heap[i]
    maxpos = max_pos(heap,i)
    while maxpos!=None and e>heap[maxpos]: 
        heap[i] = heap[maxpos]
        i = maxpos
        maxpos = max_pos(heap,i)
    heap[i] = e

def max_pos(heap,i):
    left = 2*i+1
    right = 2*i+2
    if left>=len(heap):
        return None
    elif right>=len(heap) or heap[left]>heap[right]:
        return left
    else:
        return right

def delete(v,l):
    i = 0
    while i<len(l) and l[i]!=v:
        i=i+1
    if i<len(l):
        swap(l,i,len(l)-1)
        h[:] = h[:len(l)-1]
        heapify_down(l,i)

def extract_max(heap):
    if len(heap)==0:
        return None
    else:
        max = heap[0]
        heapify_dwn(heap,0)
        return max

def swap(l,i,j):
    l[i],l[j]=l[j],l[i]

h = max_heap()
add(5,h)
add(10,h)
add(21,h)
add(0,h)
delete(21,h)
print(h)
