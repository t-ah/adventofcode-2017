from collections import defaultdict

# add all possible links recursively
def add_link(links, last_pin, strength, strengths, length):
    relev_links = list(links[last_pin])
    if len(relev_links) == 0:
        strengths.append((strength,length))
    else:
        for r_link in relev_links:
            links[r_link[1]].remove(r_link)
            if r_link[1] != r_link[2]:
                links[r_link[2]].remove(r_link)
            next_pin = 0
            if last_pin == r_link[1]:
                next_pin = r_link[2]
            else:
                next_pin = r_link[1]
            add_link(links, next_pin, strength + r_link[1] + r_link[2], strengths, length + 1)
            links[r_link[1]].add(r_link)
            links[r_link[2]].add(r_link)

strengths = []
links = defaultdict(set)
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        parts = line.strip().split("/")
        link = (i, int(parts[0]), int(parts[1]))
        links[link[1]].add(link)
        links[link[2]].add(link)

# just try everything
add_link(links, 0, 0, strengths, 0)

max_strength = 0
max_length = 0
max_length_strength = 0

for (strength, length) in strengths:
    if strength > max_strength:
        max_strength = strength
    if length > max_length:
        max_length = length
        max_length_strength = strength
    elif length == max_length and strength > max_length_strength:
        max_length_strength = strength

print("Part 1:", max_strength)
print("Part 2:", max_length_strength)