# https://careercup.com/question?id=2445

def solution(matrix):
    height, width = len(matrix), len(matrix[0])
    visited = [[0] * width for _ in range(height)]
    max_area = 0

    def count_area(x, y):
        if y < 0 or y >= height or x < 0 or x >= width or visited[y][x]:
            return 0

        visited[y][x] = 1
        if not matrix[y][x]:
            return 0
        else:
            return 1 + count_area(x - 1, y) + count_area(x + 1, y) + count_area(x, y - 1) + count_area(x, y + 1)

    for y in range(height):
        for x in range(width):
            max_area = max(count_area(x, y), max_area)

    return max_area
