class Vertex:

    def __init__(self,n):
        self.name = n
        self.neighbors = set() #to avoid duplicate, use set

    def add_neighbor(self,v):
        self.neighbors.add(v)

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False


    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key,sorted(list(self.vertices[key].neighbors)))


g =Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'),ord('H')):
    g.add_vertex(Vertex(chr(i)))


edges = {'AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ'}

for e in edges:
    g.add_edge(e[0],e[1])

g.print_graph()
