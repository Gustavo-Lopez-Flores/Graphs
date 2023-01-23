class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0]*self.vertices for i in range(self.vertices)]

  def adiciona_aresta(self, u, v, direcionado):
    if direcionado == True:
      self.grafo[u-1][v-1] = 1
    else:
      self.grafo[v-1][u-1] = 1
      self.grafo[u-1][v-1] = 1
  
  def imprime_matriz(self):
    print('Matriz:')
    for i in range(self.vertices):
      print(self.grafo[i])

  def grafo_direcionado(self):
    for i in range(self.vertices):
      for j in range(self.vertices):
        if self.grafo[i][j] != self.grafo[j][i]:
          print("Grafo Direcionado")
          return
    print("Grafo Nao Direcionado")     

g = Grafo(4)
g.adiciona_aresta(1, 2,True)
g.adiciona_aresta(2, 3,True)
g.adiciona_aresta(2, 4,False)
g.adiciona_aresta(1, 3,True)
g.imprime_matriz()
g.grafo_direcionado()

"""
def grafo_direcionado(grafo,vertices):
  for i in range(vertices):
    for j in range(vertices):
      if grafo[i][j] != grafo[j][i]:
        print("Grafo Direcionado")
        print(f"{grafo}")
        return
  print("Grafo Nao Direcionado")
  print(f"{grafo}")
        
grafo = [
[ 0, 1, 1, 1 ],
[ 1, 0, 0, 1 ],
[ 1, 0, 0, 1 ],
[ 1, 1, 1, 0 ]
]

grafo_direcionado(grafo, 4);
"""