# https://careercup.com/question?id=5740484465000448


def solution(strs):
    def common_prefix(str1, str2):
        i = 0
        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            i += 1
        return str1[:i]

    return reduce(common_prefix, strs[1:], strs[0])
