score = 0
garbage_count = 0
group_val = 0
garbage = False
skip = False

with open("input", "r") as f:
  for line in f:
    for char in line:
      if garbage and not skip:
        garbage_count += 1
      if skip:
        skip = False
      elif char == "!":
        skip = True
        if garbage: 
          garbage_count -= 1
      elif char == "{":
        if not garbage:
          group_val += 1
      elif char == "}":
        if not garbage:
          score += group_val
          group_val -= 1
      elif char == "<":
        if not garbage:
          garbage = True
      elif char == ">":
        garbage = False
        garbage_count -= 1

print score
print garbage_count
