# https://careercup.com/question?id=5705581721550848


def solution(word, words):
    words_set = set(words)

    def _solution(input_str, concatenated_so_far=list(), concatenations=list()):
        if input_str == "":
            concatenations.append(concatenated_so_far[:])
            return concatenations

        for i in range(1, len(input_str) + 1):
            if input_str[:i] in words_set:
                _solution(input_str[i:], concatenated_so_far + [input_str[:i]], concatenations)
        return concatenations

    return _solution(word)
