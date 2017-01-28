# https://www.careercup.com/question?id=6227199318294528

def solution(matrix):
    # top, bottom, left, right
    t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    res = []
    while t <= b and l <= r:

        # top
        for i in range(l, r + 1):
            res.append(matrix[t][i])
        t += 1

        # left
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        r -= 1

        # bottom
        if t <= b:
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1

        # left
        if l <= r:
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

    return res
