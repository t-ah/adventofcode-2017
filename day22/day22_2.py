from collections import defaultdict

grid = defaultdict(int)

with open("input.txt", "r") as f:
    line_no = 0
    for line in f.read().split("\n"):
        for i in range(len(line)):
            if line[i] == "#":
                grid[(line_no, i)] = 2
        line_no += 1

line_no -= 1
x, y = line_no // 2, line_no // 2

directions = [(-1,0), (0,1), (1,0), (0,-1)]
direction = 0

count = 0
for i in range(10000000):
    s = grid[(x,y)]
    if s == 0:
        direction = (direction - 1) % 4
    elif s == 1:
        count += 1
    elif s == 2:
        direction = (direction + 1) % 4
    else:
        direction = (direction + 2) % 4
    grid[(x,y)] = (s + 1) % 4
    x += directions[direction][0]
    y += directions[direction][1]

print("Part 2:", count)