def gen(val, fac, mod):
    while True:
        val = (val * fac) % 2147483647
        if val % mod == 0:
            yield val

def run(it, mod1, mod2):
    a = gen(634, 16807, mod1)
    b = gen(301, 48271, mod2)
    count = 0
    for i in range(it):
        val_a = next(a)
        val_b = next(b)
        if bin(val_a)[-16:] == bin(val_b)[-16:]:
            count += 1
    return count

print("Part 1:", run(40000000, 1, 1))
print("Part 2:", run(5000000, 4, 8))