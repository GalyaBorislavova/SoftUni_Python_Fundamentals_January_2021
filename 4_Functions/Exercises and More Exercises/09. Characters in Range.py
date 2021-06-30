char1 = input()
char2 = input()
result = ""


def characters(ch1, ch2):
    res = ""
    for chars in range(ord(ch1) + 1, ord(ch2)):
        res += chr(chars)
    return res


result += characters(char1, char2)
print(" ".join(result))