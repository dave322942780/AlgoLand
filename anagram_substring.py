# https://www.careercup.com/question?id=5389078581215232
def solution(str1, str2):
    hash_size = 26

    def get_hashed_counters(string):
        res = [0, ] * hash_size
        for char in string:
            res[ord(char) % hash_size] += 1
        return res

    str1_counters = get_hashed_counters(str1)
    sub_str_counters = get_hashed_counters(str2[0:len(str1)])

    if str1_counters == sub_str_counters:
        return True

    for i in range(len(str2) - len(str1)):
        sub_str_counters[i] -= 1
        sub_str_counters[i + len(str1)] += 1
        if str1_counters == sub_str_counters:
            return True
    return False
