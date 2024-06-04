def anagram(s: str, t: str) -> bool:
    if sorted(list(s.lower())) == sorted(list(t.lower())):
        return True
    else:
        return False