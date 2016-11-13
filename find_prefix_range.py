# a list of sorted strings, find start and end indicies of the strings with same prefix
def solution(input_strs, prefix):
    def get_idx(prefix, is_start):
        i, j = 0, len(input_strs) - 1
        idx = None
        while idx is None:
            mid = (i + j) / 2
            pre_mid = mid - 1
            post_mid = mid + 1
            if i == j:
                if not input_strs[i].startswith(prefix):
                    raise Exception("prefix not found")
                return i
            elif is_start and pre_mid < 0:
                idx = 0
            elif not is_start and post_mid > len(input_strs) - 1:
                idx = 0
            elif len(input_strs[mid]) < len(prefix):
                if input_strs[mid] < prefix[: len(input_strs[mid])]:
                    j = mid
                else:
                    i = mid
            elif input_strs[mid][: len(prefix)] == prefix:
                if is_start and input_strs[pre_mid][: len(prefix)] == prefix:
                    j = pre_mid
                elif is_start:
                    idx = mid
                if not is_start and input_strs[post_mid][: len(prefix)] == prefix:
                    i = post_mid
                elif not is_start:
                    idx = mid
            elif input_strs[mid][: len(prefix)] < prefix:
                i = mid + 1
            elif input_strs[mid][: len(prefix)] > prefix:
                j = mid - 1
        return idx

    return get_idx(prefix, True), get_idx(prefix, False)
