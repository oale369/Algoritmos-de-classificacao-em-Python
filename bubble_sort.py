# @author Alexandre Oliveira
# Exemplo de uso do bubble_sort

from timing import timed_func
import random

@timed_func
def bubble_sort(items):
    for i in range(len(items)): # Iterar a lista completa
        already_sorted = True # Definir condição de parada
        for j in range(len(items) - i - 1): # Manter uma seção crescente da lista a ser classificada
            if items[j] > items[j + 1]: # Trocar a ordem dos itens desordenados
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False # Definido como falso caso precisasse alterar
        if already_sorted:
            break
    return items

items = [random.randint(1, 1000) for _ in range(10000)]
print(bubble_sort(items)) # Inclua [1] para imprimir o tempo de execução apenas
