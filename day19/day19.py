grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(line.rstrip('\n')))

x, y = 0, 0
direction = "s"
for i in range(len(grid[0])):
    if grid[y][i] == "|":
        x = i
        y = 1
        break

steps = 0
result = ""
while True:
    steps += 1
    c = grid[y][x]
    if c == "+":
        if direction in ("n", "s"):
            if x > 0 and grid[y][x-1] not in (" ", "+", "|"):
                x -= 1
                direction = "e"
            elif x < len(grid[0]) and grid[y][x+1] not in (" ", "+", "|"):
                x += 1
                direction = "w"
            else: 
                print("weird")
                break
        elif direction in ("e", "w"):
            if y > 0 and grid[y-1][x] not in (" ", "+", "-"):
                y -= 1
                direction = "n"
            elif y < len(grid) and grid[y+1][x] not in (" ", "+", "-"):
                y += 1
                direction = "s"
            else: 
                print("weird")
                break
        continue
    elif c == " ":
        break
    if c not in ("-", " ", "|", "+"):
        result += c
    if direction == "n":
        y -= 1
    elif direction == "s":
        y += 1
    elif direction == "e":
        x -= 1
    elif direction == "w":
        x += 1
print("Part 1:", result)
print("Part 2:", steps)
