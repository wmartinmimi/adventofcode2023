class Gear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Value:
    def __init__(self, value):
        self.value = value
        self.width = 1
        while value >= 10:
            value //= 10
            self.width += 1
        self.printed = False
        self.gears = []
    def __str__(self):
        if self.printed:
            return ""
        self.printed = True
        return f"%{self.width}d" % self.value

map = []
for y in range(140):
    map.append([str(c) for c in input()])
    for x in range(140):
        try:
            _ = int(map[y][x])
            digit = 0
            for i in range(10):
                try:
                    c = int(map[y][x+i])
                    digit = digit * 10 + c
                except:
                    integer = Value(digit)
                    for j in range(i):
                        map[y][x+j] = integer
                    break
        except:
            continue

sum = 0
for y in range(140):
    for x in range(140):
        if isinstance(map[y][x], Value) or str(map[y][x]) != '*':
            continue
        prod = 1
        gear = Gear(x, y)
        no = 0
        for j in range(max(0, y-1), min(140, y+2)):
            for i in range(max(0, x-1), min(140, x+2)):
                if isinstance(map[j][i], Value):
                    if gear in map[j][i].gears:
                        continue

                    map[j][i].gears.append(gear)

                    if no > 2:
                        prod = 0
                        break
                    prod *= map[j][i].value
                    no += 1
        if no == 2:
            map[y][x] = 'X'
            sum += prod

for y in range(140):
    for x in range(140):
        print(map[y][x], end='')
    print()

print(sum)
