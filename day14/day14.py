import queue

start = "amgozmfv"

def knot(l, lengths, pos, skip):
    for length in lengths:
        if pos + length > len(l):
            offset = pos + length - len(l)
            rev = (l[pos:] + l[:offset])[::-1]
            l = rev[-offset:] + l[offset:pos] + rev[:-offset]
        else:
            l = l[:pos] + l[pos:pos + length][::-1] + l[pos + length:]
        pos = (pos + length + skip) % len(l)
        skip += 1
    return l, pos, skip

def color_group(grid, color, sx, sy):
    q = queue.Queue()
    q.put((sx,sy))
    while not q.empty():
        (x,y) = q.get()
        if x > 0 and grid[x-1][y] == "1":
            grid[x-1][y] = color
            q.put((x-1,y))
        if y > 0 and grid[x][y-1] == "1":
            grid[x][y-1] = color
            q.put((x,y-1))
        if x < 127 and grid[x+1][y] == "1":
            grid[x+1][y] = color
            q.put((x+1,y))
        if y < 127 and grid[x][y+1] == "1":
            grid[x][y+1] = color
            q.put((x,y+1))

count = 0
grid = []
for i in range(128):
    word = start + "-" + str(i)
    lengths  = [ord(c) for c in word] + [17,31,73,47,23]
    skip, pos = 0, 0
    l = [int(x) for x in range(256)]
    for _ in range(64):
        l, pos, skip = knot(l, lengths, pos, skip)
    xors = []
    for i in range(16):
        xor = l[16 * i]
        for j in range(1,16):
            xor ^= l[16*i + j]
        xors.append(xor)
    hex_data = "".join([format(x, "x").zfill(2) for x in xors])
    bin_data = bin(int(hex_data, 16))[2:].zfill(128)
    count += bin_data.count("1")
    grid.append(list(bin_data))
print("Part 1:", count)

group_count = 1
for i in range(128):
    for j in range(128):
        if grid[i][j] == "1":
            group_count += 1
            grid[i][j] = group_count
            color_group(grid, group_count, i, j)

print("Part 2:", group_count-1)