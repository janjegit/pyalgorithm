def empty():
    return ()

def is_empty(t):
    return t==()

def node(l,r,v):
    return (l,r,v)

def leaf(v):
    return node(empty(),empty(),v)

def left(t):
    return t[0]

def right(t):
    return t[1]

def value(t):
    return t[2]

def elem(t,v):
    if is_empty(t):
        return False
    elif v<value(t):
        return elem(left(t),v)
    elif v>value(t):
        return elem(right(t),v)
    else:
        return True

def add_h(t,v):
    if is_empty(t):
        return leaf(v)
    elif v<value(t):
        return node(add_h(left(t),v),right(t),value(t))
    elif v>value(t):
        return node(left(t),add_h(right(t),v),value(t))
    else:
        raise Exception('already in tree')

def add(t,v):
    try:
        return add_h(t,v)
    except Exception as e:
        if e.args[0] == 'already in tree':
            return None
        else:
            raise e

def delete(t,v):
    if is_empty(t):
        return t
    elif v<value(t):
        return node(delete(left(t),v),right(t),value(t))
    elif v>value(t):
        return node(left(t),delete(right(t),v),value(t))
    else:
        return ins_rht_into_lft(right(t),left(t))

def ins_rht_into_lft(rht_t,lft_t):
    if is_empty(lft_t):
        return rht_t
    else:
        return node(left(lft_t),ins_rht_into_lft(rht_t,right(lft_t),value(lft_t)))
