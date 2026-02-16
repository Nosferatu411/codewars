def to_jaden_case(string: str) -> str:
    return " ".join([word[0].upper() + word[1:].lower() for word in string.split()])


# Best result
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())


print(to_jaden_case("How can mirrors be real"))
