def staircase(n, display="#"):
    if 0 < n <= 30:
        result = ""
        for i in range(1, n + 1):
            result += " " * (n - i) + display * i + "\n"
        return result
