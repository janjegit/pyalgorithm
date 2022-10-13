# ADT Stack
# Konstruktoren
def empty_stack():
    return ()

def push(stack,v):
    return (stack,v)

# Selektoren
def pop(stack):
    return empty() if is_empty_stack(stack) else stack[0]

def top(stack):
    return None if is_empty_stack(stack) else stack[1]

# Testfunktionen
def is_empty_stack(stack):
    return stack==()

# ADT-Gesetze
# is_empty_stack(empty_stack()) == True
# is_empty_stack(push(stack,v)) == False
# top(empty_stack())            == None
# top(push(stack,v))            == v
# top(pop(push(stack,v)))       == top(stack)
# top(pop(pop(push(stack,v))))  == top(pop(stack))
# is_empty(pop(push(stack,v)))  == empty_stack()
