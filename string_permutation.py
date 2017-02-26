# https://careercup.com/question?id=5426694739460096


def solution(input_str):
    res = [""]
    for char in input_str:
        extended = res[:]
        for i in range(len(res)):
            res[i] += char
        res.extend(extended)
    return res
