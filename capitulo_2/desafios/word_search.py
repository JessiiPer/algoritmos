"""
Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.

A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, onde valores adjacentes
são aqueles que estão horizontalmente ou verticalmente por perto.

LEMBRE-SE: a mesma letra não pode ser usada duas vezes para construir uma palavra.

Tecnica - Deep First Search
"""

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]


def find_next_position(position, visited_positions):
    x, y = position
    possible_moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]
    


def item_value(position):
    pass
    # return board[position[0], position[1]]


def deep_first_search(position, visited_positions, word):
    if item_value(position) == word:
        return True
    next_position = find_next_position(position, visited_positions)
    if next_position:
        return deep_first_search(next_position, visited_positions + [position], word)


def solution(word):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == word[0]:
                move = (x, y)
                if deep_first_search(move, [move], word):
                    return True


print(solution('ASA'))
