buf = [0]
pos = 0
for i in range(1, 2018):
    pos = (pos + 345) % len(buf)
    pos += 1    
    buf.insert(pos, i)
print("Part 1:", buf[(pos + 1) % 2018])