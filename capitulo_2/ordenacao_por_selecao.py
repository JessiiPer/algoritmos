def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_array = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_array.append(arr.pop(menor))
    return novo_array


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
