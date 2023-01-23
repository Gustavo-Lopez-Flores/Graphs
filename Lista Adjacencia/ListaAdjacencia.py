class Grafo:
  def __init__(self, vertices):
    print('Lista:')
    self.vertices = vertices
    self.grafo = [[]for i in range(self.vertices)]
  def adiciona_aresta(self, v, u):
    self.grafo[u-1].append(v-1)
    self.grafo[v-1].append(u-1)
  def imprime_lista(self):
    for i in range(self.vertices):
      print(f'{i+1}:', end=' ')
      for j in self.grafo[i]:
        print(f'{j+1} -', end=' ')
      print('')

g = Grafo(4)
g.adiciona_aresta(1,2)
g.adiciona_aresta(2,3)
g.adiciona_aresta(2,4)
g.adiciona_aresta(3,1)
g.adiciona_aresta(4,1)
g.imprime_lista()