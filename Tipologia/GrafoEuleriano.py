def grafo_euleriano(grafo,vertices):
  par = 0
  impar = 0
  for i in range(vertices):
    soma = 0
    for j in range(vertices):
      if j != i and grafo[i][j] != 0:
        soma+=1
    if soma % 2 == 0: 
      par+=1
    else:
      impar+=1
  if par == vertices:
    print("Grafo Euleriano")
  elif impar == 2:
    print("Grafo Semi Euleriano")
  else:
    print("Grafo Nao Euleriano")
    
grafoA = [
[ 0, 1, 1, 0, 0 ],
[ 1, 0, 1, 0, 0 ],
[ 1, 1, 0, 1, 1 ],
[ 0, 0, 1, 0, 1 ],
[ 0, 0, 1, 1, 0 ]
]
grafoB = [
[ 0, 1, 1, 1, 0 ],
[ 1, 0, 1, 0, 1 ],
[ 1, 1, 0, 1, 1 ],
[ 1, 0, 1, 0, 1 ],
[ 0, 1, 1, 1, 0 ]
]
grafoC = [
[ 0, 1, 1, 1, 0 ],
[ 1, 0, 0, 1, 1 ],
[ 1, 0, 0, 1, 0 ],
[ 1, 1, 1, 0, 1 ],
[ 0, 1, 0, 1, 0 ]
]

grafo_euleriano(grafoA, 5);
grafo_euleriano(grafoB, 5);
grafo_euleriano(grafoC, 5);