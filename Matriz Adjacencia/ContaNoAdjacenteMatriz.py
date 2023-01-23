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
  def conta_nos_adjacentes(self,n):
    print('Nos adjacentes ao no (1):')
    for j in range(self.vertices):
      if self.grafo[n-1][j] != 0 and j != n-1:
        print(j+1)

g = Grafo(4)
g.adiciona_aresta(1, 1)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(2, 4)
g.adiciona_aresta(1, 3)
g.imprime_matriz()
g.conta_nos_adjacentes(1)

"""
def conta_nos_adjacentes(grafo,vertices,no):
  print('Nos adjacentes ao no (',no,'):')
  for j in range(vertices):
    if grafo[no-1][j] != 0 and j != no-1:
      print(j+1)

grafo = [
[ 0, 1, 1, 1 ],
[ 1, 0, 0, 1 ],
[ 1, 0, 0, 1 ],
[ 1, 1, 1, 0 ]
]

conta_nos_adjacentes(grafo, 4, 1);
"""