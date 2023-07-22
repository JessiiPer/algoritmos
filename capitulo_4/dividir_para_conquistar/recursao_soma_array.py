# def soma(lista):
#     total = 0
#     for x in lista:
#         total += x
#     return total

# def soma_with_recursion(lista, total=0):
#     if len(lista) == 0:
#         return total
#     total += lista[0]
#     lista.pop(0)
#     return soma_with_recursion(lista, total)

def soma_with_recursion(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_with_recursion(lista[1:])


print(soma_with_recursion([1, 4, 3, 4]))
