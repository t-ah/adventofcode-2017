from collections import defaultdict

grid = defaultdict(bool)

with open("input.txt", "r") as f:
    line_no = 0
    for line in f.read().split("\n"):
        for i in range(len(line)):
            grid[(line_no, i)] = (line[i] == "#")
        line_no += 1

line_no -= 1
x, y = line_no // 2, line_no // 2

directions = [(-1,0), (0,1), (1,0), (0,-1)]
direction = 0

count = 0
for _ in range(10000):
    if grid[(x,y)]:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
        count += 1
    grid[(x,y)] = not grid[(x,y)]
    x += directions[direction][0]
    y += directions[direction][1]

print("Part 1:", count)