from sorting_util import *
'''
Selection sort
All-Cases:  O(n^2)
Space:      O(1)
'''
def min_sort(l):
    for i in range(len(l)):
        m = min_pos(l,i)
        swap(l,m,i)

def min_pos(l,i):
    m = i
    for i in range(i+1,len(l)):
        if l[m]>l[i]:
            m = i
    return m

def swap(l,i,j):
    l[i],l[j]=l[j],l[i]

'''
Insertion sort
Best-Case: O(n)
Avg.-Case/
Worst-Case: O(n^2)
Space:      O(1)
'''
def ins_sort(l):
    for i in range(1,len(l)):
        j = i
        e = l[i]
        while j>0 and l[j-1]>e:
            l[j] = l[j-1]
            j = j-1
        l[j] = e

'''
Quick sort
Best-Case: O(n log n)
Avg.-Case: O(n log n)
Worst-Case: O(n^2)
Space:      O(log n)
'''
def qsort(l):
    qsort_h(l,0,len(l))

def qsort_h(l,start,end):
    if start+1<end:
        swap(l,start,end+(start-end)//2)
        m = s = start
        for i in range(start+1,end):
            if l[i]<l[start]:
                m = m+1
                s = s+1
                swap(l,s,i)
                swap(l,s,m)
            elif l[i]==l[start]:
                s = s+1
                swap(l,s,i)
        swap(l,start,m)
        qsort_h(l,start,m)
        qsort_h(l,m+1,end)

'''
Merge sort
All-Case: O(n log n)
Space:    O(n)
'''
def merge_sort_inpl(l):
    merge_sort_h(l,0,len(l)-1)

def merge_sort_h(l,start,end):
    if start<end:
        mid = (start+end)//2
        merge_sort_h(l,start,mid)
        merge_sort_h(l,mid+1,end)
        merge_inpl(l,start,mid,end)

def merge_inpl(l,start,mid,end):
    n1 = mid-start+1
    n2 = end-mid
    left = []
    right = []
    for i in range(max(n1,n2)):
        if i+start<len(l):
            left.append(l[i+start])
        if i+mid+1<len(l):
            right.append(l[i+mid+1])
    i = j = 0
    k = start
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            l[k] = left[i]
            i = i+1
        else:
            l[k] = right[j]
            j = j+1
        k = k+1
    while i<n1:
        l[k] = left[i]
        i = i+1
        k = k+1
    while j<n2:
        l[k] = right[j]
        j = j+1
        k = k+1

def merge_sort(l):
    if len(l)<=1:
        return l[:]
    else:
        return merge(merge_sort(l[len(l)//2:]),merge_sort(l[:len(l)//2]))

def merge(left,right):
    result = []
    i = j = 0
    for k in range(len(left)+len(right)):
        if i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i = i+1
            else:
                result.append(right[j])
                j = j+1
        else:
            new = left[i] if i<len(left) else right[j]
            result.append(new)
            i = min(i+1,len(left))
            j = min(j+1,len(right))
    return result

'''
Heap sort
All-Cases: O(n log n)
Space:     O(1)
'''
def left_pos(i):
    return i*2+1

def right_pos(i):
    return i*2+2

def parent(i):
    return (i-1)//2

def max_pos(l, n, i):
  if left_pos(i) >= n:
    return i
  k = i
  if l[k] < l[left_pos(i)]:
    k = left_pos(i)
  if right_pos(i) < n and l[k] < l[right_pos(i)]:
    k = right_pos(i)
  return k

def heapify_down(l, n, i):
  while max_pos(l, n, i) != i:
    j = max_pos(l, n, i)
    swap(l, i, j)
    i = j

def heapify_up(l,i) :
  parent_pos = parent(i)
  while parent_pos >= 0 and l[parent_pos] < l[i] :
    swap(l, parent_pos, i)
    i = parent_pos
    parent_pos = parent(i)

def build_heap(l):
  for i in range(len(l)) :
    heapify_up(l,i)

def heap_sort(l):
  build_heap(l)
  n = len(l) - 1
  for i in range(len(l)):
    swap(l, 0, n - i)
    heapify_down(l, n - i, 0)

NUM_TESTS = 5000
NUM_ELEM  = 30
print('Selection sort')
test_sort(min_sort,  NUM_TESTS, NUM_ELEM)
print('Insertion sort')
test_sort(ins_sort,  NUM_TESTS, NUM_ELEM)
print('Quick sort')
test_sort(qsort,     NUM_TESTS, NUM_ELEM)
print('Merge sort (inplace)')
test_sort(merge_sort_inpl, NUM_TESTS, NUM_ELEM)
print('Merge sort')
test_sort(merge_sort, NUM_TESTS, NUM_ELEM)
print('Heap sort')
test_sort(heap_sort, NUM_TESTS, NUM_ELEM)
