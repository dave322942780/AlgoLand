# https://careercup.com/question?id=5689327699886080


def solution(lst):
    def _solution(idx, so_far, sol):
        if idx == len(lst):
            sol.append(so_far)
        else:
            for i in range(len(lst), idx, -1):
                _solution(i, so_far + "(%s)" % "".join(map(lambda x: str(x), lst[idx:i])), sol)

        return sol

    return _solution(0, "", list())
