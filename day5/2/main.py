class Mapper:
    def __init__(self, src, des, size):
        self.src = src
        self.des = des
        self.size = size

    def useable(self, src):
        return self.src <= src < self.src + self.size

    def map(self, src):
        return src - self.src + self.des

    def compressSingle(self, map):
        print(f"compressing {self} with {map}")
        if self.des + self.size >= map.src and self.des < map.src + map.size:
            change = self.des - self.src + map.des - map.src
            src = self.src
            des = self.src + change

            b_start = max(self.des, map.src)
            b_end = min(self.des + self.size, map.src + map.size)

            size = b_end - b_start
            shift = b_start - self.des

            src += shift
            des += shift

            print(Mapper(src, des, size))
            return Mapper(src, des, size)

        else:
            return None

    def compress(self, mappers):
        new_maps = []
        for mapper in mappers:
            new_map = self.compressSingle(mapper)
            if new_map is not None:
                new_maps.append(new_map)

        return new_maps

    def __repr__(self):
        return f"Mapper(src={self.src}, des={self.des}, size={self.size})"

f = open("input.txt", "r")

lns = f.readlines()

seed_num = lns[0].split(": ")[1].split(" ")
seed_num = [int(x) for x in seed_num]

seeds = {}
for i in range(0, len(seed_num), 2):
    seeds[seed_num[i]] = seed_num[i + 1]

for ln in lns:
    print(ln)

i = 1
mappers = []
while i < len(lns):
    ln = lns[i]
    print(ln)
    if ln.strip() == "":
        i += 1
        mappers.append([])
        i += 1
        continue

    info = ln.split(" ")
    info = [int(x) for x in info]
    mappers[-1].append(Mapper(info[1], info[0], info[2]))
    i += 1

for i in range(len(mappers)):
    maps = mappers[i]
    maps = list(sorted(maps, key=lambda x: x.src))
    print(maps)
    j = 0
    while j < len(maps) - 1:
        if maps[j].src + maps[j].size < maps[j + 1].src:
            maps.insert(j + 1, Mapper(maps[j].src + maps[j].size, maps[j].src + maps[j].size, maps[j + 1].src - maps[j].src - maps[j].size))
        else:
            j += 1

    if maps[0].src != 0:
        maps.insert(0, Mapper(0, 0, maps[0].src))
    maps.append(Mapper(maps[-1].src + maps[-1].size, maps[-1].src + maps[-1].size, 1000000000))
    mappers[i] = maps

print()
print(mappers)
print(len(mappers))
print()

i = 0
while i < len(mappers) - 1:
    new_maps = []
    for map in mappers[i]:
        new_maps.extend(map.compress(mappers[i + 1]))
    mappers[i + 1] = new_maps
    print(new_maps)
    mappers.remove(mappers[i])

print()

mappers = mappers[0]

mappers = list(sorted(mappers, key=lambda x: x.des))

results = []

for seed, no in seeds.items():
    for m in mappers:
        if seed + no >= m.src and seed < m.src + m.size:
            use_seed = max(seed, m.src)
            results.append(m.map(use_seed))
            break

print(results)
print(min(results))
