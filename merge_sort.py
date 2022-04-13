# @author Alexandre Oliveira
# Exemplo de uso de merge sort, modificada para permitir classificação
# # O(n log(n)) performance - conforme ensinado pela Profa., Valéria =)
import random
import time

def merge_sorted_lists(left, right):
    left_index, right_index = 0, 0 # Início de ambas listas
    return_list = []
    while (len(return_list) < len(left) + len(right)):

        # Escolha o item mais à esquerda de cada lista que ainda não foi processada
        # Se todos forem processados, escolha um valor 'infinito' para que não considerarmos essa lista.
        left_item = left[left_index] if left_index < len(left) else float('inf')
        right_item = right[right_index] if right_index < len(right) else float('inf')
        if (left_item < right_item): # Escolha o menor item restante
            return_list.append(left_item)
            left_index += 1 # Mova na lista para não considerarmos isso novamente
        else:
            return_list.append(right_item)
            right_index += 1
    return return_list

# A classificação de mesclagem real é interessantemente simples ;)
def merge_sort(items):
    if (len(items) <= 1):
        return items
    midpoint = len(items) // 2
    left, right = items[:midpoint], items[midpoint:]

    # Divida recursivamente a lista em duas, classifique-a e, em seguida, mescle essas listas!
    return merge_sorted_lists(merge_sort(left), merge_sort(right))

rand_list = [random.randint(1, 1000) for _ in range(10000)]
start = time.perf_counter()
merge_sort(rand_list)
print(time.perf_counter() - start)
