# https://careercup.com/question?id=14948278

def _solution(string, i, j, k):
    num1 = int(string[:i])
    num2 = int(string[i:j])
    num3 = int(string[j:k])
    assert num1 + num2 == num3
    counter1 = num2
    counter2 = num3
    string = string[k:]
    while string:
        new_num = counter1 + counter2
        str_new_num = str(new_num)
        if not string.startswith(str_new_num):
            return False
        else:
            string = string[len(str_new_num):]
            counter1 = counter2
            counter2 = new_num
    return True


def solution(string):
    if len(string) < 3:
        return False
    else:
        for k in range(3, len(string) + 1):
            for j in range(2, k):
                for i in range(1, j):
                    if int(string[:i]) + int(string[i:j]) == int(string[j:k]):
                        if _solution(string, i, j, k):
                            return True
        return False
