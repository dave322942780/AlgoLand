# https://careercup.com/question?id=7617672


def solution(str_inp):
    quest_indices = []
    for i, char in enumerate(str_inp):
        if char == "?":
            quest_indices.append(i)
    res = [str_inp]
    for i in quest_indices:
        updated_res = []
        for string in res:
            str_lst = list(string)
            str_lst[i] = "0"
            updated_res.append("".join(str_lst))
            str_lst[i] = "1"
            updated_res.append("".join(str_lst))
        res = updated_res
    return res
