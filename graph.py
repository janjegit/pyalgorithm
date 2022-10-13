class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,name):
        if not name in self.graph:
            self.graph[name] = []
    
    def add_edge(self,start,weight,dest):
        self.add_node(start)
        self.add_node(dest)
        edge = (weight,dest)
        if not edge in self.graph[start]:
            self.graph[start].append(edge)

    def add_bi_edge(self,start,weight,dest):
        self.add_edge(start,weight,dest)
        self.add_edge(dest,weight,start)

    def get_graph(self):
        return self.graph

    def get_edges(self,name):
        return self.graph[name]

    def from_file(filename) :
        f = open(filename,mode='r')
        lines = f.readlines()
        f.close()
        is_directed = lines[0]=='directed\n'
        g = Graph()
        for i in range(1,len(lines)):
            colums = lines[i].strip().split(',')
            if len(colums) >= 3:
                start,weight,dest = colums[0],colums[1],colums[2]
                if is_directed:
                    g.add_edge(start,float(weight),dest)
                else:
                    g.add_bi_edge(start,float(weight),dest)                   
        return g

    def __str__(self):
        return str(self.graph)

