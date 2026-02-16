def DNA_strand(dna: str) -> str:
    l = []
    for c in dna:
        if c == "A":
            l.append("T")
        if c == "T":
            l.append("A")
        if c == "C":
            l.append("G")
        if c == "G":
            l.append("C")
    return "".join(l)


print(DNA_strand("AAATTT"))


# A / T
# C / G
