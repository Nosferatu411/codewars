def is_isogram(string: str) -> bool:
    return True if len(string) == len(set(string.lower())) else False


# Best Answer


def is_isogram(string):
    return len(string) == len(set(string.lower()))


print(is_isogram("isogram"))
print(is_isogram("teste"))
