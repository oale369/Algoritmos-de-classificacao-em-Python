# @author Alexandre Oliveira
# Função de temporização
# Uso:
# @timed_func
# def xpto_func():
#   return 5

import time
def timed_func(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return timed
