def count_items_list(lista):
    if len(lista) == 0:
        return 0
    return 1 + count_items_list(lista[1:])


print(count_items_list([2, 8, 9]))
