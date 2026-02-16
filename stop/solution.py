def spin_words(sentence):
    return " ".join(w[::-1] if len(w) >= 5 else w for w in sentence.split())
    # l = []
    # for word in sentence.split():
    #     if len(word) >= 5:
    #         l.append(word[::-1])
    #     else:
    #         l.append(word)
    # return " ".join(l)


print(spin_words("Welcome home"))
