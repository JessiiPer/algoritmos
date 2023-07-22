def solution(numbers, target_sum):
    for index_1 in range(len(numbers)):
        number1 = numbers[index_1]

        for index_2 in range(index_1 + 1, len(numbers)):
            if number1 + numbers[index_2] == target_sum:
                return [number1, numbers[index_2]]
    return []


my_array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]

print(solution(my_array, 9))
