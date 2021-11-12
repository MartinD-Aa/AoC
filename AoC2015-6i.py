import re

p1 = re.compile('.* ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

string = open('Inputs/day6.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

answer1 = 0
answer2 = 0

lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)

for c in string:
    pass

count = 0

for l in lines:
    print(count)
    count += 1
    x1, y1, x2, y2 = tuple([int(m) for m in p1.match(l).groups()])
    if 'turn on' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[x][y] = 1
    elif 'turn off' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[x][y] = 0
    elif 'toggle' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[x][y] = 1 - lights[x][y]
    else:
        print("BAD BEGINNING: {}".format(l))

print(sum(sum(l) for l in lights))

count = 0
lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)
for l in lines:
    print(count)
    count += 1
    x1, y1, x2, y2 = tuple([int(m) for m in p1.match(l).groups()])
    if 'turn on' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[x][y] += 1
    elif 'turn off' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if lights[x][y]:
                    lights[x][y] -=1
    elif 'toggle' in l:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[x][y] += 2
    else:
        print("BAD BEGINNING: {}".format(l))

print(sum(sum(l) for l in lights))