def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def empty_heap():
    return []

def add(heap,v):
    heap.append(v)
    heapify_up(heap)

def heapify_up(heap):
    i = len(heap)-1
    next_i = parent(i)
    e = heap[i]
    while i>0 and e<heap[next_i]:
        heap[i]=heap[next_i]
        i = next_i
        next_i = parent(i)
    heap[i]=e

def heapify_dwn(heap,start):
    heap[start]=heap[len(heap)-1]
    heap[:] = heap[:len(heap)-1]
    i = start
    e = heap[i]
    minpos = min_pos(heap,i)
    while minpos!=None and e>heap[minpos]: 
        heap[i] = heap[minpos]
        i = minpos
        minpos = min_pos(heap,i)
    heap[i] = e

def min_pos(heap,i):
    left = 2*i+1
    right = 2*i+2
    if left>=len(heap):
        return None
    elif right>=len(heap) or heap[left]<heap[right]:
        return left
    else:
        return right

def delete(heap,pos):
    if 0 <= pos < len(heap):
        heapify_dwn(heap,pos)
        return True
    else:
        return False

def remove(heap,v):
    i = 0
    while i<len(heap) and heap[i]!=v:
        i = i+1
    if i<len(heap):
        heapify_dwn(heap,i)
        return True
    else:
        return False

def extract_min(heap):
    if len(heap)==0:
        return None
    else:
        min = heap[0]
        heapify_dwn(heap,0)
        return min

def heapify(l):
    h = empty_heap()
    for e in l:
        add(h,e)
    return h

def heap_sort(l):
    h = heapify(l)
    result = []
    for i in range(len(l)):
        result.append(extract_min(h))
    return result

def check_heap_prop(l):
  for i in range(len(l)):
    if left(i) < len(l) and l[i] < l[left(i)]:
      return False
    if right(i) < len(l) and l[i] < l[right(i)]:
      return False
  return True

h = empty_heap()
add(h,10)
print(h)
add(h,5)
print(h)
add(h,29)
print(h)
add(h,77)
print(h)
add(h,57)
print(h)
add(h,24)
print(h)
add(h,16)
print(h)
add(h,0)
print(h)
delete(h,0)
print(h)
