def array_diff(a: list, b: list):
    return [i for i in a if i not in b]


print(array_diff([1, 2, 2], [2]))
