import random

def empty():
    return []

def is_empty(t):
    return t==[]

def node(l,r,v):
    node = [l,r,v,1]
    update_height(node)
    return node

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
    return height(right(t))-height(left(t))

def update_value(t,v):
    if not is_empty(t):
        t[2]=v

def update_height(t):
    t[3] = 1 + max(height(left(t)),height(right(t)))

def update_node(t,l,r,v):
    t[0] = l
    t[1] = r
    t[2] = v
    update_height(t)

def replace_node(t,new):
    t[:] = new

def add(t,v):
    if is_empty(t):
        replace_node(t,leaf(v))
        return True
    else:
        if v<value(t):
            res = add(left(t),v)
            update_height(t)
            rotate(t)
            return res
        elif v>value(t):
            res = add(right(t),v)
            update_height(t)
            rotate(t)
            return res
        else:
            return False

def elem(t,v):
    if is_empty(t):
        return False
    else:
        if v==value(t):
            return True
        elif v<value(t):
            return elem(left(t),v)
        else:
            return elem(right(t),v)

def delete(t,v):
    if is_empty(t):
        return t
    if v>value(t):
        update_node(t,left(t),delete(right(t),v),value(t))
    elif v<value(t):
        update_node(t,delete(left(t),v),right(t),value(t))
    else:
        if is_empty(left(t)) and is_empty(right(t)):
            replace_node(t,empty())
        elif is_empty(right(t)):
            update_node(t,left(left(t)),right(left(t)),value(left(t)))
        elif is_empty(left(t)):
            update_node(t,left(right(t)),right(right(t)),value(right(t)))
        else:
            n=left(t)
            while not is_empty(right(n)):
                n = right(n)
            n_val = value(n)
            delete(n,n_val)
            update_node(t,left(t),right(t),n_val)
#             s=successor(t,v)
#             new = delete(right(t),s)
#             update_node(t,left(t),new,s)
    if not is_empty(t):
        update_height(t)
        rotate(t)
    return t

# def successor(t,v):
#     if is_empty(t):
#         return None
#     else:
#         if value(t)<=v:
#             return successor(right(t),v)
#         else:
#             w = successor(left(t),v)
#             if w is None:
#                 return value(t)
#             else:
#                 return w

def rotate(t):
    if balance(t)==-2:
        if balance(left(t)) in [0,-1]:
            # r-rotation
            x = value(t)
            y = value(left(t))
            t1 = left(left(t))
            t2 = right(left(t))
            t3 = right(t)
            update_node(t,t1,node(t2,t3,x),y)
        else:
            # lr-rotation
            x = value(t)
            y = value(left(t))
            z = value(right(left(t)))
            t1 = left(left(t))
            t2 = left(right(left(t)))
            t3 = right(right(left(t)))
            t4 = right(t)
            update_node(t,node(t1,t2,y),node(t3,t4,x),z)
    elif balance(t)==2:
        if balance(right(t)) in [0,1]:
            # l-rotation
            x = value(t)
            y = value(right(t))
            t1 = left(t)
            t2 = left(right(t))
            t3 = right(right(t))
            update_node(t,node(t1,t2,x),t3,y)
        else:
            # rl-rotation
            x = value(t)
            y = value(right(t))
            z = value(left(right(t)))
            t1 = left(t)
            t2 = left(left(right(t)))
            t3 = right(left(right(t)))
            t4 = right(right(t))
            update_node(t,node(t1,t2,x),node(t3,t4,y),z)

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

def rand_st(n,m):
    t = empty()
    while n>0:
        v = random.randint(0,m)
        if add(t,v):
            n = n - 1
    return t

def test_tree():
    t = empty()
    quit_flg=False
    input_flg=False
    usr_mode = ''
    print('Create AVL-tree randomly (r), add nodes yourself (m) or quit (q)? ', end='')
    while not quit_flg and not input_flg:
        usr_mode = input()
        valid_modes = ['r','m','q']
        if usr_mode in valid_modes:
            input_flg = True
            if usr_mode == 'q':
                quit_flg = True
        else:
            print('Try again.')
    if not quit_flg:
        if usr_mode == 'r':
            print('Enter size of tree or quit (q): ', end='')
        elif usr_mode == 'm':
            print('Build tree from entered nodes or quit (q): ', end='')
        input_flg = False
        while not quit_flg and not input_flg:
            usr_input = input()
            if usr_input=='q':
                quit_flg == True
            elif usr_mode=='r':
                try:
                    usr_input = int(usr_input)
                except:
                    print('Enter a whole number.')
                else:
                    t = rand_st(usr_input,usr_input*10)
                    input_flg = True
            elif usr_mode=='m':
                if type(usr_input)==type('a'):
                    if len(usr_input)==1 and usr_input == 'q':
                        quit_flg == True
                    else:
                        node_lst = usr_input.split()
                        for i in range(len(node_lst)):
                            try:
                                v = int(node_lst[i])
                            except:
                                print('Only use whole numbers as node values. Try again.')
                                input_flg = False
                                break
                            else:
                                add(t,v) 
                                input_flg = True
            else:
                print('Try again.')
        if not valid(t):
            print('Failed to create valid tree.')
            print(t)
            quit_flg=True
        elif not quit_flg:
            print(t)
            while not is_empty(t) and not quit_flg:
                print(tree_to_str(t))
                usr_input = input('Remove node or quit (q): ')
                if usr_input != 'q':
                    usr_input = int(usr_input)
                    if type(usr_input)==type(42):
                        delete(t,usr_input)
                    else:
                        print('Only whole numbers allowed.')
                else:
                    quit_flg = True

test_tree()
