def solution(words, str_input):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    def pre_process(words):
        words_structure = {}
        for word in words:
            cur = words_structure
            for char in alphabets:
                count = word.count(char)
                cur.setdefault(count, {})
                cur = cur[count]
            cur[-1] = word
        return words_structure

    def get_potential_words(scrambled_str, dict):
        potential_words_queue = [dict]
        secondary_potential_words_queue = []
        potential_words = []
        for char_idx, char in enumerate(alphabets):
            cur_count = scrambled_str.count(char)
            while potential_words_queue:
                cur = potential_words_queue.pop()
                if -1 in cur:
                    potential_words.append(cur[-1])
                potential_cur_alphabet_count = filter(lambda x: x <= cur_count, cur.keys())
                secondary_potential_words_queue.extend([cur[x] for x in potential_cur_alphabet_count])
            potential_words_queue, secondary_potential_words_queue = secondary_potential_words_queue, potential_words_queue
        for potential_word in potential_words_queue:
            if potential_word[-1]:
                potential_words.append(potential_word[-1])
        return potential_words

    def get_combinations(scrambled_str, potential_words):
        def count(str_input):
            res = []
            for char_idx, char in enumerate(alphabets):
                res.append(str_input.count(char))
            return res

        def sub(counts1, counts2):
            return map(lambda x, y: x - y, counts1, counts2)

        def is_zeros(counts):
            return reduce(lambda x, y: x and y == 0, counts, True)

        def is_positives(counts):
            for i in counts:
                if i < 0:
                    return False
            return True

        def find_combination(target, so_far):
            if is_zeros(target):
                return so_far
            for potential_word in potential_words:
                sub_val = sub(target, count(potential_word))
                if is_positives(sub_val):
                    comb = find_combination(sub_val, so_far + [potential_word])
                    if comb:
                        return comb

        return find_combination(count(scrambled_str), [])

    dict = pre_process(words)
    potential_words = get_potential_words(str_input, dict)
    return get_combinations(str_input, potential_words)
