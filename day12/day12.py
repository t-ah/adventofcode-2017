from collections import defaultdict

def find_group(key, pipes):
    group = set(pipes[key])
    new_ent = pipes[key]
    while True:
        if len(new_ent) == 0:
            break
        entries = new_ent
        new_ent = []
        for e in entries:
            connected = pipes[e]
            for c in connected:
                if c not in group:
                    group.add(c)
                    new_ent.append(c)
    return group

pipes = defaultdict(list)
with open("input.txt", "r") as f:
    for line in f:
       p1 = line.strip().split(" <-> ")
       p2 = p1[1].split(", ")
       for p in p2:
           pipes[p].append(p1[0])
           pipes[p1[0]].append(p)

print("Part 1: {}".format(len(find_group("0", pipes))))

group_count = 0
all_keys = set(pipes.keys())
while len(all_keys) > 0:
    group_count += 1
    key = all_keys.pop()
    all_keys = all_keys.difference(find_group(key, pipes))
print("Part 2:", group_count)