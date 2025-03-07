def alternatingCharacters(s):
    x = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            x += 1
    return x
