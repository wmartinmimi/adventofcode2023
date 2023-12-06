
import re

f = open("input.txt", "r")

lns = f.readlines()

ln = lns[0].split(":")[1]

times = re.findall(r'\d+', ln)
times = [int(x) for x in times]


ln = lns[1].split(":")[1]

records = re.findall(r'\d+', ln)
records = [int(x) for x in records]

way = 1
for [time, record] in zip(times, records):
    cw = 0
    for i in range(time):
        print(f"{i} * {time - i} = {i * (i - time)}")
        if i * (time - i) >= record:
            cw += 1
    way *= cw
    
print(way)
