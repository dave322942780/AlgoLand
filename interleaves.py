# https://careercup.com/question?id=14539805

def solution_test_interleave(str1, str2, str):
    def _test_interleave(str1, str2, str):
        if str1 == "" and str2 == "" and str == "":
            return True

        return (str1 and str and str1[0] == str[0] and _test_interleave(str1[1:], str2, str[1:])) or \
               (str2 and str and str2[0] == str[0] and _test_interleave(str1, str2[1:], str[1:]))

    return _test_interleave(str1, str2, str)


def solution_gen_interleaves(str1, str2):
    def _gen_interleaves(str1, str2, str="", res=[]):
        if not str1 and not str2:
            res.append(str)
        if str1:
            _gen_interleaves(str1[1:], str2, str + str1[0], res)
        if str2:
            _gen_interleaves(str1, str2[1:], str + str2[0], res)
        return res

    return _gen_interleaves(str1, str2)
