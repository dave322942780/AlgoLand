# https://www.careercup.com/question?id=11070934

def solution(lst):
    boundary_record = {}
    max_range = None
    max_length = 0
    
    for elem in input_set:
        if elem in boundary_record:
            pass
        else:
            left_most = right_most = elem
            if elem - 1 in boundary_record:
                left_most = boundary_record[elem - 1]
            if elem + 1 in boundary_record:
                right_most = boundary_record[elem + 1]
            if right_most - left_most > max_length:
                max_length = right_most - left_most
                max_range = [left_most, right_most + 1]
            boundary_record[left_most] = right_most
            boundary_record[right_most] = left_most
    return None if not max_range else range(max_range[0], max_range[1])
