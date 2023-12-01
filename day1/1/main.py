sum = 0
for _ in range(1000):
    ln = input()
    i = 0
    j = len(ln) - 1
    c1, c2 = None, None
    while c1 is None:
        try:
            c1 = int(ln[i])
        except:
            i += 1

    while c2 is None:
        try:
            c2 = int(ln[j])
        except:
            j -= 1
    sum += c1 * 10 + c2
print(sum)

