from graph import Graph

g = Graph.from_file('nikolaus.csv')

def eulerpath_h(g,solutions,path,node,size):
    if len(path)==size:
        solutions += [path]
    else:
        succs = g.get_edges(node)
        for edge,next_node in succs:
            if not edge in path:
                result = eulerpath_h(g,solutions,path+[edge],next_node,size)
                if result:
                    solutions += path
                    return solutions

def nikolaus(g):
    solutions = []
    for node in g.graph:
        eulerpath_h(g,solutions,[],node,8)
    return solutions

print(nikolaus(g))
