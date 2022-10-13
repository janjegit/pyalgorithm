def bla(n):
    if n==0:
        return 1
    else:
        return 2*blub(bla(n-1),1)

def blub(n,r):
    if n==0:
        return r
    else:
        return 1+blub(n-1,r)

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

def bla_iter(n):
    st = stack()
    rt = stack()
    st = push(('bla',n),st)
    while not empty_stack(st):
        nxt = top(st)
        st = pop(st)
        fun = nxt[0]
        if fun=='bla':
            n = nxt[1]
            if n==0:
                rt = push(1,rt)
            else:
                rt = push(2,rt)
                st = push(('*',),st)
                st = push(('blub',1),st)
                st = push(('bla',n-1),st)
        elif fun=='blub':
            n = top(rt)
            rt = pop(rt)
            rt = push(blub_iter(n,1),rt)
        elif fun=='*':
            f0 = top(rt)
            rt = pop(rt)
            f1 = top(rt)
            rt = pop(rt)
            rt = push(f0*f1,rt)
    return top(rt)

def blub_iter(n,r):
    st = stack()
    rt = stack()
    st = push(('blub',n,r),st)
    while not empty_stack(st):
        nxt = top(st)
        st = pop(st)
        fun = nxt[0]
        if fun=='blub':
            n = nxt[1]
            r = nxt[2]
            if n==0:
                rt = push(r,rt)
            else:
                rt = push(1,rt)
                st = push(('+',),st)
                st = push(('blub',n-1,r),st)
        elif fun=='+':
            s0 = top(rt)
            rt = pop(rt)
            s1 = top(rt)
            rt = pop(rt)
            rt = push(s0+s1,rt)
    return top(rt)

print(bla(5))
print(bla_iter(5))
