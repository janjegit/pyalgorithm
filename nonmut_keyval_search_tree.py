def empty_store():
    return []

def node(l,r,k,v):
    return [l,r,k,v]

def leaf(k,v):
    return node(empty_store(),empty_store(),k,v)

def left(t):
    return t[0]

def right(t):
    return t[1]

def key(t):
    return t[2]

def value(t):
    return t[3]

def lookup(t,k):
    if is_empty(t):
        return False
    elif k<key(t):
        return lookup(left(t),k)
    elif k>key(t):
        return lookup(right(t),k)
    else:
        return value(t)

def insert(t,k,v):
    if is_empty(t):
        return leaf(k,v)
    elif k<key(t):
        return node(insert(left(t),k,v),right(t),key(t),value(t))
    elif k>key(t):
        return node(left(t),insert(right(t),k,v),key(t),value(t))
    else:
        return node(left(t),right(t),k,v)

def delete(t,k):

