
total = 0
for card in range(0, 203):
    ln = input()
    points = ln.split(":")[1].split("|")
    win = points[0].strip().split(" ")
    win = filter(lambda x: x != "", win)
    win = list(map(lambda x: int(x), win))
    got = points[1].strip().split(" ")
    got = filter(lambda x: x != "", got)
    got = list(map(lambda x: int(x), got))

    current = list(set(win) & set(got))
    if len(current) > 0:
        cp = 1
        for i in range(1, len(current)):
            cp *= 2
        total += cp

print(total)
