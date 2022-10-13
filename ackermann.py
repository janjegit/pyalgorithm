def stack():
    return ()

def empty_stack(s):
    return s==()

def push(v,s):
    return (v,s)

def pop(s):
    return stack() if empty_stack(s) else s[1]

def top(s):
    return None if empty_stack(s) else s[0]

def ackermann(n,m):
    if n==0:
        return m+1
    elif m==0:
        return ackermann(n-1,1)
    else:
        return ackermann(n-1,ackermann(n,m-1))

def ackermann_iter(n,m):
    s = stack()
    r = stack()
    s = push(('ack',n,m),s)
    while not empty_stack(s):
        nxt = top(s)
        if len(nxt)==2:
            n=nxt[1]
            arg = top(r)
            r = pop(r)
            nxt = ('ack',n,arg)
        s = pop(s)
        fun = nxt[0]
        if fun=='ack':
            n=nxt[1]
            m=nxt[2]
            if n==0:
                r = push(m+1,r)
            elif m==0:
                s = push(('ack',n-1,1),s)
            else:
                s = push(('ack',n-1),s)
                s = push(('ack',n,m-1),s)
    return top(r)
