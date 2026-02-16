def find_short(s: str) -> int:
    return len(sorted(s.split(), key=len))


print(find_short("bitcoin take over the world maybe who knows perhaps"))
