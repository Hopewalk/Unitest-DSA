def funnyString(s):
    c = "".join(reversed(list(s)))
    traget = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(c[i]) - ord(c[i - 1])):
            traget = False

    if traget is True:
        return "Funny"
    else:
        return "Not Funny"
