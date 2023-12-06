
import re
import math

f = open("input.txt", "r")

lns = f.readlines()

ln = lns[0].split(":")[1]

times = re.findall(r'\d+', ln)
times = ["".join(times)]
times = [int(x) for x in times]


ln = lns[1].split(":")[1]

records = re.findall(r'\d+', ln)
records = ["".join(records)]
records = [int(x) for x in records]

way = 1
for [time, record] in zip(times, records):
    end = int(time / 2 + math.sqrt(time ** 2 / 4 - record) + 1)
    start = int(time / 2 - math.sqrt(time ** 2 / 4 - record) + 1)
    way *= (end - start)
    
print(way)
