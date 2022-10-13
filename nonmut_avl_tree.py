def empty():
    return ()

def is_empty(t):
    return t==()

def node(l,r,v):
    return (l,r,v,1+max(height(l),height(r)))

def leaf(v):
    return node(empty(),empty(),v)

def left(t):
    return t[0]

def right(t):
    return t[1]

def value(t):
    return t[2]

def height(t):
    return 0 if is_empty(t) else t[3]

def balance(t):
    return 0 if is_empty(t) else height(right(t))-height(left(t))

def add_h(t,v):
    if is_empty(t):
        return leaf(v)
    elif v<value(t):
        result = node(add_h(left(t),v),right(t),value(t))
        return rotate(result)
    elif v>value(t):
        result = node(left(t),add_h(right(t),v),value(t))
        return rotate(result)
    else:
        raise Exception('already in tree')

def add(t,v):
    try:
        return add_h(t,v)
    except Exception as e:
        if e.args[0]=='already in tree':
            return None
        else:
            raise e

def delete(t,v):
    if is_empty(t):
        return t
    elif v<value(t):
        return rotate(node(delete(left(t),v),right(t),value(t)))
    elif v>value(t):
        return rotate(node(left(t),delete(right(t),v),value(t)))
    else:
        return insert_rht_in_lft(left(t),right(t))

def insert_rht_in_lft(lft_t,rht_t):
    if is_empty(lft_t):
        return rht_t
    else:
        return node(left(lft_t),insert_rht_in_lft(rht_t,right(lft_t)),value(lft_t))

def rotate(t):
    if balance(t)==2:
        if balance(left(t)) in [0,1]:
            # l-rotation
            x = value(t)
            y = value(right(t))
            t1 = left(t)
            t2 = left(right(t))
            t3 = right(right(t))
            return node(node(t1,t2,x),t3,y)
        else:
            # rl-rotation
            x = value(t)
            y = value(right(t))
            z = value(left(right(t)))
            t1 = left(t)
            t2 = left(left(right(t)))
            t3 = right(left(right(t)))
            t4 = right(right(t))
            return node(node(t1,t2,x),node(t3,t4,y),z)
    elif balance(t)==-2:
        if balance(right(t)) in [0,-1]:
            # r-rotation
            x = value(t)
            y = value(left(t))
            t1 = left(left(t))
            t2 = right(left(t))
            t3 = right(t)
            return node(t1,node(t2,t3,x),y)
        else:
            # lr-rotation
            x = value(t)
            y = value(left(t))
            z = value(right(left(t)))
            t1 = left(left(t))
            t2 = left(right(left(t)))
            t3 = right(right(left(t)))
            t4 = right(t)
            return node(node(t1,t2,y),node(t3,t4,x),z)
    else:
        return t

def valid_left(t,v):
    return is_empty(t) or value(t) < v and \
           valid_left(left(t),v) and \
           valid_left(right(t),v)

def valid_right(t,v):
    return is_empty(t) or value(t) > v and \
           valid_right(left(t),v) and \
           valid_right(right(t),v)

def valid(t):
    return is_empty(t) or valid_left(left(t), value(t)) and \
           valid_right(right(t), value(t)) and \
           valid(left(t)) and valid(right(t))

def tree_to_str(t):
    if is_empty(t):
        return ''
    else:
        res = str(value(t)) + ' (' + str(height(t)) + '|'+ str(balance(t)) +')'
        ptr_right = '└── '
        ptr_left =  '├── ' if not is_empty(right(t)) else ptr_right 
        res += traverse_nodes(left(t) , '', ptr_left,  is_empty(right(t)) == False) 
    res += traverse_nodes(right(t), '', ptr_right, False)
    return res

def traverse_nodes(t,pad,ptr,has_rht_child):
    if is_empty(t):
        return ''
    else:
        res='\n'+pad+ptr+str(value(t))+' ('+str(height(t))+'|'+str(balance(t))+')'
        pad_both = pad + '│   ' if has_rht_child else pad + '    '
        ptr_right = '└── '
        ptr_left =  '├── ' if not is_empty(right(t)) else ptr_right 
        res += traverse_nodes(left(t),pad_both,ptr_left,is_empty(right(t))==False) 
        res += traverse_nodes(right(t),pad_both,ptr_right,False)
        return res
