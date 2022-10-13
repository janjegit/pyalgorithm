def empty() :
    return []

def node(l,v,r) :
    return [l,v,r]

def leaf(v) :
    return node(empty(),v,empty())

def is_empty(tree) :
    return tree == []

def left(tree) :
    return tree[0]

def value(tree) :
    return tree[1]

def right(tree) :
    return tree[2]

def update_node(new_tree,tree) :
    tree[:] = new_tree

def update_value(v,tree) :
    tree[1] = v
    
def tree_at(path,tree) :
    if len(path) == 0 :
        return tree
    elif is_empty(tree) :
        return None
    elif path[0]=='l' :
        return tree_at(path[1:],left(tree))
    else :
        return tree_at(path[1:],right(tree))
    
# mutate value in tree at given positon (path)
def update_value_at(path,v,tree) :
    if len(path) == 0 :
        update_value(v,tree)
    elif is_empty(tree) :
        return None
    elif path[0]=='l' :
        return update_value_at(path[1:],v,left(tree))
    else :
        return update_value_at(path[1:],v,right(tree))

# replace complete subtree in tree at given postion (path)
def update_tree_at(path,new_tree,tree) :
    if len(path) == 0 :
        # return update_node(new_tree,tree) # Achtung, s.u,
        return update_node(copy_tree(new_tree), tree)
    elif is_empty(tree) :
        return None
    elif path[0]=='l' :
        return update_tree_at(path[1:],new_tree,left(tree))
    else :
        return update_tree_at(path[1:],new_tree,right(tree))

# Beachte, dass diese Implementierung sich leider nicht an den
# Merksatz der Vorlesung hält. Es gibt mutierende Opearationen auf den
# Binärbäumen. Deshalb darf die Funktion update_tree_at ihr Argument,
# welches sie nicht mutiert, nicht unkopiert zurückgeben und auch nicht
# unkopiert in den Binärbaum einfügen. Für den Pfad '' tut sie dies
# aber direkt für den übergebenen einzufügenden Binärbaum, bzw. fügt
# diesen bei allen anderen Pfaden unkopiert ein. Deshalb ist es sinnvoll,
# den Baum als Kopie einzugüfen:
def copy_tree(tree) :
    if is_empty(tree) :
        return empty()
    else :
        return node(copy_tree(left(tree)), value(tree), copy_tree(right(tree)))
    
exp = node(leaf(32),'+',node(leaf(7),'*',node(leaf(1),'+',leaf(2))))

print(exp)
print(tree_at('rr',exp)) 
print(tree_at('rl',exp))
print(tree_at('rlrl',exp))

update_tree_at('rr',leaf(3),exp)
update_value_at('r','/',exp)

print(exp)