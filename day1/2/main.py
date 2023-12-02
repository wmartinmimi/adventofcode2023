sum = 0


def isDigit(text):
    if text[:3] == 'one':
        return 1
    if text[:3] == 'two':
        return 2
    if text[:5] == 'three':
        return 3
    if text[:4] == 'four':
        return 4
    if text[:4] == 'five':
        return 5
    if text[:3] == 'six':
        return 6
    if text[:5] == 'seven':
        return 7
    if text[:5] == 'eight':
        return 8
    if text[:4] == 'nine':
        return 9
    return None


for _ in range(1000):
    ln = input()
    i = 0
    j = len(ln) - 1
    c1, c2 = None, None
    while c1 is None:
        try:
            c1 = isDigit(ln[i:])
            c1 = int(ln[i])
        except:
            i += 1

    while c2 is None:
        try:
            c2 = isDigit(ln[j:])
            c2 = int(ln[j])
        except:
            j -= 1
    sum += c1 * 10 + c2
print(sum)

