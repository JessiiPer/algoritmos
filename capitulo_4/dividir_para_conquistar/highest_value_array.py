def highest_value_array(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    else:
        value = highest_value_array(array[1:])
        if value > array[0]:
            return value
        else:
            return array[0]


print(highest_value_array([1, 3, 4]))
