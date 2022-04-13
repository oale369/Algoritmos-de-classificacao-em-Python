# @author Alexandre Oliveira
# Exemplo de uso de insertion sort, modificada para permitir classificação
# O(n^2) no pior cenário - conforme ensinado pela Profa., Valéria =)

from timing import timed_func
import random

@timed_func
def insertion_sort(items, left=0, right=None):
    if right is None: # Se padrão, ordenamos a lista por completa
        right = len(items) - 1
    for i in range(left + 1, right + 1): # Se direita for len(items) - 1, isso ordena a lista completa
        current_item = items[i]
        j = i - 1 # Escolher o item antes do item atual

        while (j >= left and current_item < items[j]): # Quebre quando o item atual estiver no lugar certo
            items[j + 1] = items[j] # Movendo este item para cima
            j -= 1 # Percorrendo "para a esquerda" ao longo da lista
        
        items[j + 1] = current_item # Insira current_item em seu local correto

    return items

items = [random.randint(1, 1000) for _ in range(1000)]
print(insertion_sort(items)) # Inclua [1] para imprimir o tempo de execução apenas
