import random
import time

def pesquisa_binaria(v, p, r, x):
    #condição de parada ou de existência
    if p <= r:
       q = (p+r) // 2 #indice no meio do vetor
       if x > v[q]:
           return pesquisa_binaria(v, p+1, r, x)
       elif x < v[q]:
           return pesquisa_binaria(v, p-1, r, x)
       else:
           return q #encontrou o elemento

    return -1 #não encotrou o elemento

vetor = list(range(0,20))
chave = 2
antes = time.time()
posicao = pesquisa_binaria(vetor, 0, len(vetor)-1,chave)
depois = time.time()
total = (depois-antes) * 1000 #cálculo de tempo gasto para o resultado

if posicao >= 0:
    print(f"O elemento {chave} foi encontrado na posição {posicao}")
else:
    print(f"O elemento {chave} não foi encontrado")
print(f"O tempo total gasto foi de %0.2f ms" %total)
print(vetor)