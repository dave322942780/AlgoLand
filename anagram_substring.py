# https://www.careercup.com/question?id=5389078581215232
def solution(str1, str2):
    hash_size = 1024
    str1_counter = [0, ] * hash_size
    for char in str1:
        str1_counter[ord(char) % hash_size] += 1

    for i in range(len(str2) - len(str1)):
        counter = [0, ] * hash_size
        sub_str = str2[i:i + len(str1)]
        for char in sub_str:
            counter[ord(char) % hash_size] += 1
        if counter == str1_counter:
            return True
    return False
