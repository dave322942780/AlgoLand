# https://careercup.com/question?id=19300678

def solution(num):
    num_to_letter_mapping = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _solution(number, word="", words=list()):
        if not number:
            words.append(word)
            return
        valid_num = number[0]
        number = number[1:]
        is_break = False

        while int(valid_num) < len(num_to_letter_mapping) and not is_break:
            letter = num_to_letter_mapping[int(valid_num)]
            _solution(number, word + letter, words)

            if number:
                valid_num += number[0]
                number = number[1:]
            else:
                is_break = True
        return words

    return _solution(str(num))
