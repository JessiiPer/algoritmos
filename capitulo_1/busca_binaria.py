"""
    A pesquisa binária é um algoritmo.
    Sua entrada é uma lista ordenada de elementos.
    Se o elemento que voce está buscando está na lista, a pesquisa binária retorna sua localização.
    Caso contrário, a pesquisa binária retorna None

    Na busca binária o tempo de execução é executada com tempo logaritmo
"""


def pesquisa_binaria(lista, item):
    baixo: int = 0
    alto: int = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        index_meio = round(meio)
        chute = lista[index_meio]
        if chute == item:
            return index_meio
        if chute > item:
            return index_meio - 1
        else:
            baixo = index_meio + 1
    return None


minha_lista = [1, 2, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 5))
