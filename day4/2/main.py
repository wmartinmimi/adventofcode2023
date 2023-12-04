
total = 0
def getNewCards(ln):
    points = ln.split(":")[1].split("|")
    win = points[0].strip().split(" ")
    win = filter(lambda x: x != "", win)
    win = list(map(lambda x: int(x), win))
    got = points[1].strip().split(" ")
    got = filter(lambda x: x != "", got)
    got = list(map(lambda x: int(x), got))

    current = list(set(win) & set(got))
    return len(current)

lns = []
copies = [1]
for card in range(203):
    ln = input()
    lns.append(ln)
    copies.append(1)

card = 0
maxCard = 0
while card < 203:
    new = getNewCards(lns[card])
    print(f"{card + 1} {copies[card]} {new} {card + new}")
    for i in range(new):
        if card + i >= 203:
            break
        copies[card + i + 1] += copies[card]
    if maxCard < card + new:
        maxCard = card + new
    card += 1

total = 0
for i in range(0, 203):
    total += copies[i]

print(total)
