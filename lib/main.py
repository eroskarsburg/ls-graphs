class Vertice:
    def __init__(self, vertice_id):
        self.id = vertice_id
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.visitados = {}

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.id not in self.vertices:
            self.vertices[vertice.id] = vertice
            return True
        else:
            return False
        
    def add_arresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(v2)
            self.vertices[v2].add_neighbor(v1)
            return True
        else:
            return False
        
    def get_vertices(self):
        return self.vertices.keys()
    
    ##def set_visitados(self):
        
    
    def __iter__(self):
        return iter(self.vertices.values())
    

def processa_caminho(v, g):
    # Pegar o anterior do vertice atual



    
def dfs(Grafo, start: int, goal: int) -> (int, float, [int]): # type: ignore
    assert start in Grafo.vertices
    assert goal in Grafo.vertices
    S = []
    S.append(start)
    while not len(S)== 0:
        v = S.pop()
        print(v, end=' ')
        # if goal == g:
        #     return v
        # if not visitados(v):
        #     processa_caminho(v, g)
        #     set_visitados(v)
        #     for u in Grafo.neighbors(v):
        #         S.append(u)
        

grafo = Grafo()
for i in range(4):
    grafo.add_vertice(Vertice(i))
grafo.add_arresta(0, 1)
grafo.add_arresta(0, 2)
grafo.add_arresta(1, 2)
grafo.add_arresta(1, 3)
grafo.add_arresta(2, 3)