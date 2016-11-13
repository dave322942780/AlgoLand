# given a map, find the x, y coordinate for which the coordinate yields the max horizontal and vertical hits
# this is a google on site interview question
def solution(map):

    if not map or not map[0]:
        return

    v_counts = [0] * len(map[0])
    v_max = 0
    v_max_idx = 0

    h_counts = [0] * len(map)
    h_max = 0
    h_max_idx = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                h_counts[i] += 1
                v_counts[j] += 1
                if v_counts[j] > v_max:
                    v_max = h_counts[j]
                    v_max_idx = j
                if h_counts[i] > h_max:
                    h_max = h_counts[i]
                    h_max_idx = i
    return v_max_idx, h_max_idx
