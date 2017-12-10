inp = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"

lengths = [int(x) for x in inp.split(",")]

skip = 0
pos = 0
l = [int(x) for x in range(256)]

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

l, _, _ = knot(l, lengths, pos, skip)
print "Part 1:", l[0] * l[1]

lengths2  = [ord(c) for c in inp] + [17,31,73,47,23]
skip, pos = 0, 0
l = [int(x) for x in range(256)]

for _ in range(64):
  l, pos, skip = knot(l, lengths2, pos, skip)

xors = []
for i in range(16):
  xor = l[16 * i]
  for j in range(1,16):
    xor ^= l[16*i + j]
  xors.append(xor)

print "Part 2:", "".join([format(x, "x") for x in xors])
