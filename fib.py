def stack():
    return ()

def empty_stack(s):
    return s==()

def top(s):
    return None if empty_stack(s) else s[0]

def push(v,s):
    return (v,s)

def pop(s):
    return stack() if empty_stack(s) else s[1]

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_iter(n):
    s = stack()
    r = stack()
    s = push(('fib',n),s)
    while not empty_stack(s):
        nxt = top(s)
        s = pop(s)
        if nxt[0]=='fib':
            n = nxt[1]
            if n==0:
                r = push(0,r)
            elif n==1:
                r = push(1,r)
            else:
                s = push(('+',),s)
                s = push(('fib',n-1),s)
                s = push(('fib',n-2),s)
        elif nxt[0]=='+':
            r0= top(r)
            r = pop(r)
            r1= top(r)
            r = pop(r)
            r = push(r0+r1,r)
    return top(r)
