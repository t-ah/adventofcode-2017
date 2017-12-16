def dance(progs, moves, cache):
    key = repr(progs)
    if key in cache:
        return cache[key][:]
    for m in moves:
        if m.startswith("s"):
            l = int(m[1:])
            progs = progs[-l:] + progs[:-l]
        elif m.startswith("x"):
            ind = [int(i) for i in m[1:].split("/")]
            progs[ind[0]], progs[ind[1]] = progs[ind[1]], progs[ind[0]]
        elif m.startswith("p"):
            names = m[1:].split("/")
            ind = [progs.index(names[0]), progs.index(names[1])]
            progs[ind[0]], progs[ind[1]] = progs[ind[1]], progs[ind[0]]
    cache[key] = progs
    return progs[:]

progs = [chr(i) for i in range(ord('a'),ord('p')+1)]
moves = []
cache = {}
with open("input.txt", "r") as f:
    moves = f.read().strip().split(",")

progs = dance(progs, moves, cache)    
print("Part 1:", "".join(progs))

for i in range(1000000000 - 1): # this may take a while
    progs = dance(progs, moves, cache) 
print("Part 2:", "".join(progs))