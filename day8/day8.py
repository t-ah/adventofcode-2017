from collections import defaultdict

reg = defaultdict(int)
max2 = 0

def do(parts):
  regName = parts[0]
  opVal = int(parts[2])
  if parts[1] == "dec":
    opVal *= -1
  reg[regName] += opVal
  return reg[regName]

# b inc 5 if a > 1
with open("input", "r") as f:
  for line in f.readlines():
    parts = line.split(" ")
    regName = parts[4]
    compVal = parts[6]
    if (parts[5] == ">" and reg[regName] > int(compVal)) or (parts[5] == "<" and reg[regName] < int(compVal)) or (parts[5] == ">=" and reg[regName] >= int(compVal)) or (parts[5] == "<=" and reg[regName] <= int(compVal)) or (parts[5] == "==" and reg[regName] == int(compVal)) or (parts[5] == "!=" and reg[regName] != int(compVal)):
      m = do(parts)
      if m > max2:
        max2 = m

  max = 0
  for r in reg:
    if reg[r] > max:
      max = reg[r]
  print("Part 1:", max)
  print("Part 2:", max2)