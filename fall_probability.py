# http://www.careercup.com/question?id=15556758
# difficulty: 2
# length: 2


def solution(x, y, size, step):
    if step == 0 and 0 <= x < size and 0 <= y < size:
        return 1
    elif step > 0 and 0 <= x < size and 0 <= y < size:
        return (solution(x + 1, y, size, step - 1) +
                solution(x - 1, y, size, step - 1) +
                solution(x, y + 1, size, step - 1) +
                solution(x, y - 1, size, step - 1)) / 4.0
    return 0
