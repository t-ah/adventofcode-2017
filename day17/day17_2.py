pos = 0
pos0 = 0
val = 0
for i in range(1, 50000000):
    pos = (pos + 345) % i
    if pos == pos0:
        val = i
    elif pos < pos0:
        pos0 += 1
    pos += 1

print("Part 2:", val)