from collections import defaultdict

def get_val(reg, addr):
    try:
        a = int(addr)
        return a
    except ValueError:
        return reg[addr]

prog = []
with open("input.txt", "r") as f:
    prog = [x.split(" ") for x in f.read().split("\n")]
    
pc = 0
reg = defaultdict(int)
count = 0

while pc >= 0 and pc < len(prog):
    instr = prog[pc]
    if instr[0] == "set":
        reg[instr[1]] = get_val(reg, instr[2])
    elif instr[0] == "sub":
        reg[instr[1]] -= get_val(reg, instr[2])
    elif instr[0] == "mul":
        reg[instr[1]] *= get_val(reg, instr[2])
        count += 1
    elif instr[0] == "jnz":
        if get_val(reg, instr[1]) != 0:
            pc = pc + get_val(reg, instr[2]) - 1
    pc += 1

print("Part 1:", count)