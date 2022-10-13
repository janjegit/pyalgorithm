'''
Best-Case:  O(1)
Avg.-Case:  O(log n)
Space:      O(1)
'''
def bin_search_h(l,v,start,end):
    if start<end:
        m = end+(start-end)//2
        if v==l[m]:
            return m
        elif v<l[m]:
            return bin_search_h(l,v,start,m)
        else:
            return bin_search_h(l,v,m+1,end)
    else:
        return None

def bin_search(l,v):
    return bin_search_h(l,v,0,len(l))
