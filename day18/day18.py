from collections import defaultdict

def get_val(reg, addr):
    try:
        a = int(addr)
        return a
    except ValueError:
        return reg[addr]

prog = []
pc = 0
reg = defaultdict(int)
with open("input.txt", "r") as f:
    for line in f:
        prog.append(line.strip().split(" "))

last_snd = 0
while pc >= 0 and pc < len(prog):
    instr = prog[pc]
    if instr[0] == "snd":
        last_snd = get_val(reg, instr[1])
    elif instr[0] == "set":
        reg[instr[1]] = get_val(reg, instr[2])
    elif instr[0] == "add":
        reg[instr[1]] += get_val(reg, instr[2])
    elif instr[0] == "mul":
        reg[instr[1]] *= get_val(reg, instr[2])
    elif instr[0] == "mod":
        reg[instr[1]] %= get_val(reg, instr[2])
    elif instr[0] == "rcv":
        if last_snd != 0:
            break
    elif instr[0] == "jgz":
        if get_val(reg, instr[1]) > 0:
            pc += get_val(reg, instr[2]) - 1
    pc += 1

print("Part 1:", last_snd)