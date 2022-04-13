# @author Alexandre Oliveira
# Exemplo de uso de quicksort
# No local, mas não estável

import random
import time

def quicksort(items):
    if (len(items) <= 1):
        return items
    pivot = random.choice(items)
    less_than_pivot = [x for x in items if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items if x > pivot]

    # Divide recursivamente a lista em itens maiores que, menores que,
    # e igual a um pivô escolhido, então combine as listas como usando recursão.
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

items = [random.randint(1, 1000) for _ in range(1000)]
start = time.perf_counter()
quicksort(items)
print(time.perf_counter() - start)
