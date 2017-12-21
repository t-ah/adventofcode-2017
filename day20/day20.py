import re, sys
from collections import defaultdict

pat = re.compile("p=<(.+),(.+),(.+)>, v=<(.+),(.+),(.+)>, a=<(.+),(.+),(.+)>")

particles = []
with open("input.txt", "r") as f:
    for line in f:
        particles.append([int(x) for x in pat.match(line).group(1,2,3,4,5,6,7,8,9)])

# Part 1
min_a = sys.maxsize
res = 0
for i in range(len(particles)):
    p = particles[i]
    sum_a = sum([abs(x) for x in p[6:9]])
    if sum_a < min_a:
        min_a = sum_a
        res = i
print("Part 1:", res)

# Part 2
for n in range(1000): # (without ending detection, yet this is more than enough)
    print(n, len(particles))
    by_p = defaultdict(list)
    for i in range(len(particles)):
        p = particles[i]
        p[3] += p[6]
        p[4] += p[7]
        p[5] += p[8]
        p[0] += p[3]
        p[1] += p[4]
        p[2] += p[5]
        by_p[(p[0], p[1], p[2])].append(p)
    particles = []
    for ps in by_p.values():
        if len(ps) == 1:
            particles.append(ps[0])

print("Maybe Part 2:", len(particles))