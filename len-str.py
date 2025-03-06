def length_lastword(s: str) -> int:
    words = s.strip().split()
    return len(words[-1]) if words else 0

s = input("enter a string: ")
print(length_lastword(s))