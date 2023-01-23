class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0]*self.vertices for i in range(self.vertices)]
  def adiciona_aresta(self, u, v):
    self.grafo[u-1][v-1] = 1
    self.grafo[v-1][u-1] = 1
  def imprime_matriz(self):
    print('Matriz de adjacências:')
    for i in range(self.vertices):
      print(self.grafo[i])
      
g = Grafo(4)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(2, 4)
g.adiciona_aresta(1, 3)
g.imprime_matriz()