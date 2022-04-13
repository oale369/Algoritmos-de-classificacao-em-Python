# @author Alexandre Oliveira
# Um TimSort simplificado (para prj de análise ver alg real para precisão)
# Uso de estratégias de classificação por inserção e mesclagem para produzir uma
# classificação estável e rápida através de execuções existentes nos dados

from insertion_sort import insertion_sort
from merge_sort import merge_sorted_lists

def timsort(items):
    min_subsection_size = 32

    # Classifica cada subseção de tamanho 32
    # O algoritmo real (projetos de análise) escolhe cuidadosamente um tamanho de subseção para desempenho
    for i in range(0, len(items), min_subsection_size):
        insertion_sort(items, i, min((i + min_subsection_size - 1), len(items) - 1))

    # Percorra a lista de subseções e mescle-as usando merge_sorted_lists
    size = min_subsection_size
    while size < len(items):    
        for start in range(0, len(items), size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (len(items) - 1)) # aritmética para indexar corretamente

            # Mesclar usando merge_sorted_lists
            merged_array = merge_sorted_lists(
                items[start:midpoint + 1], 
                items[midpoint + 1:end + 1])
            
            items[start:start + len(merged_array)] = merged_array # Inserir matriz mesclada
        size *= 2 # Dobre o tamanho dos 'pedaços mesclados' a cada vez até atingir a lista inteira
    
    return items