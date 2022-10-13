import math

from graph import Graph

class ToDo:
    def __init__(self):
        self.lookup = {}
        self.heap   = []

    def is_empty(self):
        return self.heap==[]

    def _min_pos(self,i):
        left = lambda x : 2*x+1
        right = lambda x : 2*x+2
        k = i
        if left(i)<len(self.heap) and self.heap[k][0]>self.heap[left(i)][0]:
            k = left(i)
        if right(i)<len(self.heap) and self.heap[k][0]>self.heap[right(i)][0]:
            k = right(i)
        return k

    def _heapify_down(self,i):
        m = self._min_pos(i)
        self.lookup[self.heap[i][1]]=i
        while m!=i:
            self.heap[i],self.heap[m]=self.heap[m],self.heap[i]
            self.lookup[self.heap[i][1]]=i
            i = m
            m = self._min_pos(i)
        self.lookup[self.heap[i][1]]=i

    def _heapify_up(self):
        parent = lambda x : (x-1)//2
        i = len(self.heap)-1
        self.lookup[self.heap[i][1]]=i
        p = parent(i)
        while p>=0 and self.heap[p][0]>self.heap[i][0]:
            self.heap[i],self.heap[p]=self.heap[p],self.heap[i]
            self.lookup[self.heap[i][1]]=i
            i = p
            p = parent(i)
        self.lookup[self.heap[i][1]]=i

    def add(self,vertex):
        name = vertex[1]
        if name in self.lookup:
            pos = self.lookup[name]
            self.heap[pos] = vertex
        else:
            self.heap.append(vertex)
            self._heapify_up()

    def extract_min(self):
        if self.is_empty():
            return None
        else:
            m = self.heap[0][1]
            self.heap[0] = self.heap.pop()
            self.lookup.pop(m)
            self._heapify_down(0)
            return m

    def __str__(self):
        return str(self.heap)

def dijstras_shortest_path(graph,start,dest):

    def set_distance(vertices,name,new_distance):
        vertices[name][0] = new_distance

    def get_distance(vertices,name):
        return float(vertices[name][0])

    def set_prev_vertex(vertices,name,prev):
        vertices[name][2] = prev

    def get_prev_vertex(vertices,name):
        return vertices[name][2]

    def set_as_visited(vertices,name):
        vertices[name][1] = True

    def was_visited(vertices,name):
        return vertices[name][1]

    vertices = {}
    todo = ToDo()
    for name in graph.get_graph():
        vertices[name] = [math.inf,False,'']

    current_vertex = start
    set_distance(vertices,start,0)
    while get_distance(vertices,current_vertex)<math.inf and current_vertex != dest:

        for distance,neighbour in graph.get_edges(current_vertex):
            if not was_visited(vertices,neighbour):
                old_distance = get_distance(vertices,neighbour)
                new_distance = float(distance) + get_distance(vertices,current_vertex)
                if old_distance > new_distance:
                    set_distance(vertices,neighbour,new_distance)
                    set_prev_vertex(vertices,neighbour,current_vertex)
                    todo.add((new_distance,neighbour))                
        set_as_visited(vertices,current_vertex)
        current_vertex = todo.extract_min()

    if get_distance(vertices,current_vertex)==math.inf:
        return None
    else:
        path = []
        while current_vertex != '':
            path.insert(0,current_vertex)
            current_vertex = get_prev_vertex(vertices,current_vertex)
        return (get_distance(vertices,dest),path)

g = Graph.from_file('map_kiel_city.csv')
start = input('Start: ')
dest  = input('Ziel:  ')
link = 'https://www-ps.informatik.uni-kiel.de/~fhu/CGI/route/path.cgi?path='
route = dijstras_shortest_path(g,start,dest)[1]
result = ''
for i in range(len(route)):
    result = result+route[i]
    if i<len(route)-2:
        result = result + ','
print(link+result)
