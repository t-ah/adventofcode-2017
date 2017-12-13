def check_delay(data, delay):
    for depth in data:
        if (depth + delay) % data[depth] == 0:
            return False
    return True

data = {}
with open("input.txt", "r") as f:
    sev = 0
    for line in f:
        spl = line.strip().split(": ")
        depth, rng = int(spl[0]), int(spl[1])
        effective_rng = 2 * rng - 2
        data[depth] = effective_rng        
        if depth % effective_rng == 0:
            sev += rng * depth
    print("Part 1:", sev)

delay = 0
while True:
    # this is a good candidate for optimization
    if check_delay(data, delay):
        print("Part 2:", delay)
        break
    delay += 1