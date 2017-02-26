def no_multiply_op(a, b):
    res = 0
    while b:
        if b & 1:
            res += a
        b >>= 1
        a <<= 1
    return res


def no_add_op(a, b):
    while b:
        c = (a & b) << 1
        a ^= b
        b = c
    return a


def no_exponent_op(a, b):
    res = 1
    while b:
        if b & 1:
            res *= a
        b >>= 1
        a <<= 1
    return res
