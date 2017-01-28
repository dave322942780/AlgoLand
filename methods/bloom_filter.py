# http://www.cse.yorku.ca/~oz/hash.html
def find_intersection_bloom_filter(lst1, lst2):
    vector = [False, ] * 2048

    def djb2_hash(input_string):
        hashed_val = 5381
        for char in input_string:
            hashed_val = ((hashed_val << 5) + hashed_val) + ord(char)
        return hashed_val

    def sdbm_hash(input_string):
        hashed_val = 0
        for char in input_string:
            hashed_val = ord(char) + (hashed_val << 6) + (hashed_val << 16) - hashed_val
        return hashed_val

    def lose_lose_hash(input_string):
        hashed_val = 0
        for char in input_string:
            hashed_val += ord(char)
        return hashed_val

    def xor_hash(input_string):
        hashed_val = 0
        for char in input_string:
            hashed_val ^= ord(char)
        return hashed_val

    def peek(func, input_string, input_vector):
        return input_vector[func(input_string) % len(input_vector)]

    def mark_visited(func, input_string, input_vector):
        input_vector[func(input_string) % len(input_vector)] = True

    hash_funcs = [djb2_hash, sdbm_hash, lose_lose_hash, xor_hash]
    for lst1_item in lst1:
        for hash_func in hash_funcs:
            mark_visited(hash_func, lst1_item, vector)

    res = []
    for lst2_item in lst2:
        in_all_hashed = True
        for hash_func in hash_funcs:
            in_all_hashed &= peek(hash_func, lst2_item, vector)
        if in_all_hashed:
            res.append(lst2_item)
    return res


assert ["gh", "ij", "kl", "mn", "op"] == find_intersection_bloom_filter(
    ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op"],
    ["gh", "ij", "kl", "mn", "op", "qr", "st", "uv", "wx", "yz"])
