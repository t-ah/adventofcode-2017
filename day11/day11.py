from collections import Counter

# order does not matter, count all moves that do not cancel each other out
with open("input", "r") as f:
  directions = f.read().strip().split(",")
  cnt = Counter()
  for d in directions:
    cnt[d] += 1
  n = cnt["n"] - cnt["s"]
  n_add = min(cnt["ne"], cnt["nw"])
  n += n_add
  cnt["ne"] -= n_add
  cnt["nw"] -= n_add
  n_sub = min(cnt["sw"], cnt["se"])
  n -= n_sub
  cnt["se"] -= n_sub
  cnt["sw"] -= n_sub
  final_mod = abs((cnt["ne"] + cnt["se"]) - (cnt["nw"] + cnt["sw"]))

  print "Part 1:", n + final_mod

  # new approach for part 2, count horizontal and vertical distance
  hor, vert, max_dist = 0, 0, 0
  for d in directions:
    if d == "s":
      vert -= 1
    elif d == "n":
      vert += 1
    elif d == "ne":
      vert += 0.5
      hor += 1
    elif d == "nw":
      vert += 0.5
      hor -= 1
    elif d == "sw":
      vert -= 0.5
      hor -= 1
    elif d == "se":
      vert -= 0.5
      hor += 1  
    
    # with each horizontal step, half a vertical step is done automatically    
    dist = hor + (vert - hor * 0.5)
    max_dist = max(dist, max_dist)
  
  print "Part 2:", max_dist

