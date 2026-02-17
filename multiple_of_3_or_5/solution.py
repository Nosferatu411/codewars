def solution(number):
    return sum(x for x in range(number) if not x % 5 or not x % 3)


print(solution(10))
