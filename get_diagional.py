# https://www.careercup.com/question?id=5661939564806144

def get_left_down_diagonal_lst(matrix, x, y, x_length, y_length):
    lst = []
    while x >= 0 and y < y_length:
        lst.append(matrix[y][x])
        x -= 1
        y += 1
    return lst


def solution(matrix):
    if len(matrix) == 0:
        return []
    res = []
    x_length = len(matrix[0])
    y_length = len(matrix)
    for x in range(x_length):
        res.append(get_left_down_diagonal_lst(matrix, x, 0, x_length, y_length))

    for y in range(1, y_length):
        res.append(get_left_down_diagonal_lst(matrix, x_length - 1, y, x_length, y_length))
    return res
