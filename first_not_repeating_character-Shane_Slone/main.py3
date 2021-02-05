def first_not_repeating_character(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1
    for key in d:
        if d[key] == 1:
            return key
    return "_"
