# https://careercup.com/question?id=19638671

def solution(num):
    accumulator = 0
    for i in xrange(1, num + 1, 2):
        accumulator += i
        if accumulator == num:
            return True
        elif accumulator > num:
            return False
