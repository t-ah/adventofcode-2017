def rotate(square):
    if len(square) == 5:
        return square[3] + square[0] + "/" + square[4] + square[1]
    else:
        return square[8] + square[4] + square[0] + "/" + square[9] + square[5] + square[1] + "/" + square[10] + square[6] + square[2]

def flip_h(square):
    if len(square) == 5:
        return square[3] + square[4] + "/" + square[0] + square[1]
    else:
        return square[8:11] + "/" + square[4:7] + "/" + square[0:3]

def flip_v(square):
    if len(square) == 5:
        return square[1] + square[0] + "/" + square[4] + square[3]
    else:
        return square[2] + square[1] + square[0] + "/" + square[6] + square[5] + square[4] + "/" + square[10] + square[9] + square[8]

grid = [".#.", "..#", "###"]

# setup rules incl. rotates and flips
rules = {}
with open("input.txt", "r") as f:
    for line in f:
        parts = line.strip().split(" => ")
        lhs, rhs = parts[0], parts[1]
        for _ in range(4):
            lhs = rotate(lhs)
            rules[lhs] = rhs
            rules[flip_h(lhs)] = rhs
            rules[flip_v(lhs)] = rhs

# iterate line by line of squares
for c in range(18):
    new_grid = []
    if len(grid) % 2 == 0:
        for i in range(int(len(grid) / 2)):
            for k in range(3):
                new_grid.append("")
            for j in range(int(len(grid) / 2)):
                square = grid[2*i][2*j:2*j+2] + "/" + grid[2*i+1][2*j:2*j+2]
                res = rules[square].replace("/", "")
                for k in range(3):
                    new_grid[3*i + k] += res[3*k:3*k + 3]
    else:
        for i in range(int(len(grid) / 3)):
            for k in range(4):
                new_grid.append("")
            for j in range(int(len(grid) / 3)):
                square = grid[3*i][3*j:3*j+3] + "/" + grid[3*i+1][3*j:3*j+3] + "/" + grid[3*i+2][3*j:3*j+3]
                res = rules[square].replace("/", "")
                for k in range(4):
                    new_grid[4*i + k] += res[4*k:4*k + 4]
    grid = new_grid
    if c == 4:
        count = 0
        for l in grid:
            count += l.count("#")
        print("Part 1:", count)

count = 0
for l in grid:
    count += l.count("#")
print("Part 2:", count)