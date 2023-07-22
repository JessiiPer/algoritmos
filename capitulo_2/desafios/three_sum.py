"""
A idéia deste problema é identificar todos os três números que quando somados resultem em um valor especificado.
Exemplos
Se o array é [12, 3, 1, 2, -6, 5, -8, 6] e o target é 0. Neste caso, seu programa deve retornar:
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]
A soma de todos os valores das listas acima será igual a zero.
"""


def solution(numbers, target_sum):
    result = []
    sorted_array = list(sorted(numbers))
    for current_point in range(len(numbers)):
        right_point = len(numbers) - 1
        left_point = current_point + 1
        while left_point < right_point:
            pointers_sum = sorted_array[current_point] + sorted_array[left_point] + sorted_array[right_point]
            if pointers_sum < target_sum:
                left_point += 1
            elif pointers_sum > target_sum:
                right_point -= 1
            else:
                result.append([sorted_array[current_point], sorted_array[left_point], sorted_array[right_point]])
                left_point += 1
                right_point -= 1
    return result


my_array = [12, 3, 1, 2, -6, 5, -8, 6]

print(solution(my_array, 0))
