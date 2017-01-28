# https://www.careercup.com/question?id=5179916190482432

def solution(lst):
    if not lst:
        return lst
    front_products = [1]
    rear_products = [1]
    res = []
    for i in lst:
        front_products.append(i * front_products[-1])
    for i in range(len(lst) - 1, -1, -1):
        rear_products.append(rear_products[-1] * lst[i])
    for i in range(len(lst)):
        res.append(front_products[i] * rear_products[len(rear_products) - i - 2])
    return res
