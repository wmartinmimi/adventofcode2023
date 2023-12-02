
sum = 0

r, g, b = 12, 13, 14
for no in range(1, 101):
    ln = input()
    games = ln.split(':')[1].split(';')
    cr, cg, cb = 0, 0, 0
    for game in games:
        colors = game.strip().split(',')
        colors = list(map(lambda x: x.strip().split(' '), colors))
        for i in range(0, len(colors)):
            if colors[i][1] == 'red':
                cr = max(cr, int(colors[i][0]))
            elif colors[i][1] == 'green':
                cg = max(cg, int(colors[i][0]))
            elif colors[i][1] == 'blue':
                cb = max(cb, int(colors[i][0]))
    product = cr * cg * cb
    sum += product

print(sum)
            
