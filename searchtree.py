def empty():
    return []

def is_empty(t):
    return t==[]

def node(l,r,v):
    return [l,r,v]

def leaf(v):
    return [empty(),empty(),v]

def left(t):
    return t[0]

def right(t):
    return t[1]

def value(t):
    return t[2]

def replace_node(old,new):
    old[:]=new

def update_node(t,l,r,v):
    t[0] = l
    t[1] = r
    t[2] = v

def elem(t,v):
    if is_empty(t):
        return False
    elif v<value(t):
        return elem(left(t),v)
    elif v>value(t):
        return elem(right(t),v)
    else:
        return True

def add(t,v):
    if is_empty(t):
        replace_node(t,leaf(v))
        return True
    elif v<value(t):
        return add(left(t),v)
    elif v>value(t):
        return add(right(t),v)
    else:
        return False

def delete(t,v):
    if is_empty(t):
        return False
    elif v<value(t):
        return delete(left(t),v)
    elif v>value(t):
        return delete(right(t),v)
    else:
        remove_node(t)

def remove_node(t):
    if is_empty(left(t)) and is_empty(right(t)):
        replace_node(t,empty())
    elif is_empty(left(t)):
        update_node(t,left(right(t)),right(right(t)),value(right(t)))
    elif is_empty(right(t)):
        update_node(t,left(left(t)),right(left(t)),value(left(t)))
    else:
        n = left(t)
        while not is_empty(right(n)):
            n = right(n)
        val_n = value(n)
        delete(n,val_n)
        update_node(t,left(t),right(t),val_n)
