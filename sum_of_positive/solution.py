def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:


            sum = sum + number

    return sum


# Best Answer


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


print(positive_sum([1, -4, 7, 12]))
