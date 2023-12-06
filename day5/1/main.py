class Mapper:
    def __init__(self, ln):
        info = ln.split(" ")
        info = [int(x) for x in info]
        self.src = info[1]
        self.des = info[0]
        self.size = info[2]

    def useable(self, src):
        return self.src <= src < self.src + self.size

    def map(self, src):
        return src - self.src + self.des

    def __repr__(self):
        return f"Mapper(src={self.src}, des={self.des}, size={self.size})"

f = open("input.txt", "r")

lns = f.readlines()

seeds = lns[0].split(": ")[1].split(" ")
seeds = [int(x) for x in seeds]

i = 1
mappers = []
while i < len(lns):
    ln = lns[i]
    if ln.strip() == "":
        i += 1
        mappers.append([])
        i += 1
        continue

    print(ln)
    mappers[-1].append(Mapper(ln))
    i += 1

for mapper in mappers:
    for i in range(len(seeds)):
        for m in mapper:
            if m.useable(seeds[i]):
                seeds[i] = m.map(seeds[i])
                break    

print(mappers)
   
print(seeds)
print(min(seeds))
