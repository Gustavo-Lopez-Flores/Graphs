import heapq 

n, m = input().split()
n = int(n) 
m = int(m)

H = []

for j in range(m):   
    a, b, c = input().split()  
    a = int(a)
    b = int(b)
    c = int(c)  
    heapq.heappush(H, (c, a, b))  

C = [[] * n for i in range(n)]  

for i in range(n):
    C[i].append(i)   

S = [] 

for i in range(n):
    S.append(i)

cont = 0   
custo = 0  

while cont < n-1:
    c, a, b = heapq.heappop(H) 
    if S[a] != S[b]: 
        custo = custo + c 
        p = S[a]  
        q = S[b]  
        if q < p: 
            p, q = q, p
        for j in C[q]: 
            S[j] = p   
        C[p].extend(C[q]) 
        C[q] = []        
        cont = cont + 1  
      
print(f"Custo Minimo: {custo}")

'''
ENTRADA DE DADOS
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 5 4
2 8 2
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7
'''