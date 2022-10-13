import random

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
        res = str(value(t))
        ptr_right = '└── '
        ptr_left =  '├── ' if not is_empty(right(t)) else ptr_right 
        res += traverse_nodes(left(t) , '', ptr_left,  is_empty(right(t)) == False) 
    res += traverse_nodes(right(t), '', ptr_right, False)
    return res

def traverse_nodes(t,pad,ptr,has_rht_child):
    if is_empty(t):
        return ''
    else:
        res = '\n' + pad + ptr + str(value(t))
        pad_both = pad + '│   ' if has_rht_child else pad + '    '
        ptr_right = '└── '
        ptr_left =  '├── ' if not is_empty(right(t)) else ptr_right 
        res += traverse_nodes(left(t) , pad_both, ptr_left , is_empty(right(t)) == False) 
        res += traverse_nodes(right(t), pad_both, ptr_right, False)
        return res

# def rand_st(n,m):
#     t = empty()
#     while n>0:
#         if add(t,random.randint(0,m)):
#             n = n - 1
#     return t
